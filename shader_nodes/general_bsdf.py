import bpy, mathutils

# This material requires a custom attribute.
# To automate the creation of this attribute (for an object), see set_object_colour.py

# Note that when used in a geometry node, the attribute type needs to change from "Object" to "Geometry"

mat = bpy.data.materials.new(name="GeneralBSDF")
mat.use_nodes = True

# initialize GeneralBSDF node group
def generalbsdf_node_group():
    generalbsdf = mat.node_tree
    # start with a clean node tree
    for node in generalbsdf.nodes:
        generalbsdf.nodes.remove(node)
    generalbsdf.color_tag = 'NONE'
    generalbsdf.description = ""
    
    # generalbsdf interface
    
    # initialize generalbsdf nodes
    # node Principled BSDF
    principled_bsdf = generalbsdf.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # Roughness
    principled_bsdf.inputs[2].default_value = 0.5
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Subsurface Weight
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[8].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf.inputs[9].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf.inputs[11].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[12].default_value = 0.5
    # Specular Tint
    principled_bsdf.inputs[13].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[14].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[15].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[16].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[17].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[18].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[19].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[20].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[21].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[22].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[23].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[24].default_value = 0.5
    # Sheen Tint
    principled_bsdf.inputs[25].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[27].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[29].default_value = 1.3300000429153442
    
    # node Material Output
    material_output = generalbsdf.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0
    
    # node Attribute
    attribute = generalbsdf.nodes.new("ShaderNodeAttribute")
    attribute.name = "Attribute"
    attribute.attribute_name = "Object Colour"
    attribute.attribute_type = 'OBJECT'
    
    # Set locations
    principled_bsdf.location = (10.0, 300.0)
    material_output.location = (297.8846130371094, 326.4835205078125)
    attribute.location = (-336.1431884765625, 300.1494140625)
    
    # Set dimensions
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    material_output.width, material_output.height = 140.0, 100.0
    attribute.width, attribute.height = 140.0, 100.0
    
    # initialize generalbsdf links
    # attribute.Vector -> principled_bsdf.Base Color
    generalbsdf.links.new(attribute.outputs[1], principled_bsdf.inputs[0])
    # principled_bsdf.BSDF -> material_output.Surface
    generalbsdf.links.new(principled_bsdf.outputs[0], material_output.inputs[0])
    # attribute.Alpha -> principled_bsdf.Alpha
    generalbsdf.links.new(attribute.outputs[3], principled_bsdf.inputs[4])
    return generalbsdf


generalbsdf = generalbsdf_node_group()

