import bpy
# Remove weird shading that sometimes appears when using obj files taken from the internet
# This is equivalent to going into an object -> data -> geometry data -> clear custom split normals
bpy.ops.object.select_all(action="SELECT")
selection = bpy.context.selected_objects
bpy.ops.object.select_all(action="DESELECT")

for o in selection:
    if o.type == "MESH":
        bpy.context.view_layer.objects.active = o
        bpy.ops.mesh.customdata_custom_splitnormals_clear()
