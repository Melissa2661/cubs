import bpy
import os
import bmesh


def export_per_object(export_dir, selected_objects=None):
    os.makedirs(export_dir, exist_ok=True)
    if selected_objects is None:
        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
    #
    if not selected_objects:
        return
    #
    # Save selection
    #
    original_active = bpy.context.view_layer.objects.active
    original_selection = bpy.context.selected_objects.copy()
    #
    for obj in selected_objects:
        bpy.ops.object.select_all(action='DESELECT')
        #
        # Duplicate data
        #
        obj_copy = obj.copy()
        obj_copy.data = obj.data.copy()
        bpy.context.collection.objects.link(obj_copy)
        #
        obj_copy.select_set(True)
        bpy.context.view_layer.objects.active = obj_copy
        bpy.ops.object.convert(target='MESH')
        #
        # Export
        #
        export_path = os.path.join(export_dir, f"{obj.name}.obj")
        bpy.ops.wm.obj_export(
            filepath=export_path,
            export_selected_objects=True,
            export_triangulated_mesh=True,
            forward_axis='X',
            up_axis='Z'
        )
        print(f"Exported: {export_path}")
        bpy.data.objects.remove(obj_copy, do_unlink=True)
    #
    # Restore selection
    #
    bpy.ops.object.select_all(action='DESELECT')
    for obj in original_selection:
        obj.select_set(True)
    #
    bpy.context.view_layer.objects.active = original_active
