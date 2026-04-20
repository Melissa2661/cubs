import bpy
from mathutils import Vector

# See general_bsdf.py for the associated shader node

context = bpy.context
obj = context.object

def setup_object_colour(obj=None):
    """
    Function that creates the custom attribute required by the GeneralBSDF material.
    """
    if obj is None:
        obj = bpy.context.active_object
    if not obj:
        print("No object active.")
        return
    attr_name = "Object Colour"
    #
    # Create the colour attribute
    if attr_name not in obj:
        obj[attr_name] = Vector((1, 1, 1, 1))
    #
    # Set some properties so that the colour can be edited from the UI
    ui = obj.id_properties_ui(attr_name)
    ui.update(description="Object colour for General BSDF material")
    ui.update(default=Vector((1, 1, 1, 1)))
    ui.update(min=0)
    ui.update(max=1)
    ui.update(subtype="COLOR")

