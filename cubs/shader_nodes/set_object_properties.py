import bpy
from mathutils import Vector


# See general_bsdf.py for the associated shader node
def setup_object_colour(obj=None, colour=(1.0, 1.0, 1.0, 1.0), attr_name="Object Colour", description=None):
    """
    Function that creates the custom attribute required by the GeneralBSDF material.
    See general_bsdf.py or general_bsdf_4_4.py for the associated shader
    """
    if obj is None:
        obj = bpy.context.active_object
    if not obj:
        print("No object active.")
        return
    #
    if description is None:
        description = attr_name
    # Create the colour attribute
    if attr_name not in obj:
        obj[attr_name] = colour
    #
    # Set some properties so that the colour can be edited from the UI
    ui = obj.id_properties_ui(attr_name)
    ui.update(description=description)
    ui.update(default=(1.0, 1.0, 1.0, 1.0))
    ui.update(min=0.0)
    ui.update(max=1.0)
    ui.update(subtype="COLOR")


def setup_object_float(obj=None, val=0.5, min=0.0, max=1.0, attr_name="Fac", description=None):
    """
    Function that creates a custom float.
    """
    if obj is None:
        obj = bpy.context.active_object
    if not obj:
        print("No object active.")
        return
    #
    if description is None:
        description = attr_name
    # Create the float
    if attr_name not in obj:
        obj[attr_name] = val
    ui = obj.id_properties_ui(attr_name)
    ui.update(description=description)
    ui.update(default=0.0)
    ui.update(min=min)
    ui.update(max=max)
    
    
def setup_wireframe_properties(obj=None, colour=(1.0, 1.0, 1.0, 1.0)):
    """
    Function that creates the custom attribute required by the GeneralWireframe material.
    See wireframe_bsdf.py for the associated shader
    """
    print(colour[0], colour[1], colour[2])
    setup_object_colour(obj=obj, colour=colour, attr_name="Object Colour", description="Colour for general BSDF")
    setup_object_colour(obj=obj, colour=(0.0, 0.0, 0.0, 1.0), attr_name="Wireframe Colour", description="Colour of Wireframe")
    setup_object_float(obj=obj, val=0.001, attr_name="Wireframe Width", description="Width of Wireframe")
    
    