import bpy
# In the context of terrain creation, it was necessary to extract
#       the new position / radius information created by geometry nodes.
#       The following code was made for this.


depsgraph = bpy.context.evaluated_depsgraph_get()
object_we_care_about = bpy.data.objects["Plane"]
with open("extract_info.txt", "w") as f:
    for object_instance in depsgraph.object_instances:
        # This is an object which is being instanced.
        obj = object_instance.object
        # `is_instance` denotes whether the object is coming from instances (as an opposite of
        # being an emitting object. )
        # if not object_instance.is_instance:
        #    print(f"Object {obj.name} at {object_instance.matrix_world}")
        if object_instance.is_instance and obj == object_we_care_about:
            # Instanced will additionally have fields like uv, random_id and others which are
            # specific for instances. See Python API for DepsgraphObjectInstance for details,
            print(f"Instance of {obj.name} at {object_instance.matrix_world}")
            t = object_instance.matrix_world.translation
            s = object_instance.matrix_world.median_scale
            f.write(f"{t[0]} {t[1]} {t[2]} {s}\n")
