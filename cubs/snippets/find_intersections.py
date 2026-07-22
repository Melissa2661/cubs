import bpy
import bmesh
from mathutils import bvhtree


def _build_bvh(obj, EPSILON=0.0001):
    """
    Build a BVH tree in world space for a mesh object.
    """
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval = obj.evaluated_get(depsgraph)
    mesh = obj_eval.to_mesh()
    bm = bmesh.new()
    bm.from_mesh(mesh)
    # Transform vertices into world space
    bm.transform(obj.matrix_world)
    bvh = bvhtree.BVHTree.FromBMesh(bm, epsilon=EPSILON)
    bm.free()
    obj_eval.to_mesh_clear()
    return bvh


def _show_selection(selected):
    """
    Extra logic that makes newly selected vertices actually selected in edit mode next time the user opens edit mode.
    """
    def switch_mode(obj):
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')
    
    temp = bpy.context.view_layer.objects.active
    if selected is list:
        for o in selected:
            switch_mode(o)
    else:
        switch_mode(selected)
    bpy.context.view_layer.objects.active = temp


def find_self_intersections(obj=None):
    """
    Find all self-intersections, and select them on the mesh.
    """
    if obj is None:
        obj = bpy.context.active_object
    if not obj or obj.type != 'MESH':
        raise Exception("Invalid object")
    mesh = obj.data
    mesh.calc_loop_triangles()
    world_verts = [obj.matrix_world @ v.co for v in mesh.vertices]
    #
    # Turn polygons to triangles
    triangles = [tuple(lt.vertices) for lt in mesh.loop_triangles]
    if not triangles:
        raise Exception("No triangles found.")
    #
    # BVH
    bvh = bvhtree.BVHTree.FromPolygons(world_verts, triangles, all_triangles=True)
    if bvh is None:
        raise Exception("Failed to build BVH.")
    #
    # Intersect
    pairs = bvh.overlap(bvh)
    intersecting_tris = set()
    for i, j in pairs:
        if i == j:
            continue
        intersecting_tris.add(i)
        intersecting_tris.add(j)
    #
    # Map triangle indices back to polygons
    #
    intersecting_polys = set(mesh.loop_triangles[i].polygon_index for i in intersecting_tris)
    #
    # Deselect all and select intersecting polygons
    #
    for p in mesh.polygons:
        p.select = False
    for pi in intersecting_polys:
        mesh.polygons[pi].select = True
    #
    _show_selection(obj)
    #
    if len(intersecting_polys) == 0:
        print("No intersections found.")
    else:
        print(f"Found {len(intersecting_polys)} intersecting polygons.")
    return intersecting_polys, intersecting_tris


def find_intersections(selected=None):
    if selected is None:
        selected = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
    if len(selected) < 2:
        raise Exception("Less that two meshes selected.")
    #
    # Build BVHs
    #
    bvhs = {}
    for obj in selected:
        bvhs[obj.name] = _build_bvh(obj)
    #
    intersections_found = False
    for i in range(len(selected)):
        for j in range(i + 1, len(selected)):
            obj_a = selected[i]
            obj_b = selected[j]
            bvh_a = bvhs[obj_a.name]
            bvh_b = bvhs[obj_b.name]
            overlaps = bvh_a.overlap(bvh_b)
            if overlaps:
                intersections_found = True
                print(f"INTERSECTION: '{obj_a.name}' / '{obj_b.name}'")
                print(f"    Found {len(overlaps)} intersecting polygons.")
                for (a, b) in overlaps:
                    obj_a.polygons[a].select = True
                    obj_b.polygons[b].select = True
    #
    if not intersections_found:
        print("No intersections found.")
        return
    _show_selection(selected)
