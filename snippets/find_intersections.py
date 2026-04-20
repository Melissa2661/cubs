import bpy
from mathutils import bvhtree


def find_self_intersections(obj=None):
    """
    Find all self-intersections, and select them in Edit mode.
    """
    if obj is None:
        obj = bpy.context.active_object
    if not obj or obj.type != 'MESH':
        print("No mesh object active.")
        return
    mesh = obj.data
    mesh.calc_loop_triangles()
    #
    # Build world-space vertex list
    world_verts = [obj.matrix_world @ v.co for v in mesh.vertices]
    #
    # Build triangle index lists from loop_triangles
    triangles = [tuple(lt.vertices) for lt in mesh.loop_triangles]
    if not triangles:
        print("No triangles found.")
        return
    #
    # Build BVH for triangles
    bvh = bvhtree.BVHTree.FromPolygons(world_verts, triangles, all_triangles=True)
    if bvh is None:
        print("Failed to build BVH.")
        return
    #
    # Find overlapping triangle pairs
    pairs = bvh.overlap(bvh)
    intersecting_tris = set()
    for i, j in pairs:
        if i == j:
            continue
        intersecting_tris.add(i)
        intersecting_tris.add(j)
    #
    # Map triangle indices to original polygon indices (select whole polygon containing the tri)
    intersecting_polys = set(mesh.loop_triangles[i].polygon_index for i in intersecting_tris)
    #
    # Deselect all and select intersecting polygons
    for p in mesh.polygons:
        p.select = False
    for pi in intersecting_polys:
        mesh.polygons[pi].select = True
    #
    # Ensure the selection is visible in Edit Mode
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode='OBJECT')
    #
    if len(intersecting_polys) == 0:
        print("No intersections found.")
    else:
        print(f"Selected {len(intersecting_polys)} polygon(s).")
    return intersecting_polys, intersecting_tris
