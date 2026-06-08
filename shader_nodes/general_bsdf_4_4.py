import bpy
import mathutils
import os
import typing


generalbsdf = bpy.data.materials.new(name="GeneralBSDF")
if bpy.app.version < (5, 0, 0):
    generalbsdf.use_nodes = True


generalbsdf.alpha_threshold = 0.5
generalbsdf.line_priority = 0
generalbsdf.max_vertex_displacement = 0.0
generalbsdf.metallic = 0.0
generalbsdf.paint_active_slot = 0
generalbsdf.paint_clone_slot = 0
generalbsdf.pass_index = 0
generalbsdf.refraction_depth = 0.0
generalbsdf.roughness = 0.4000000059604645
generalbsdf.show_transparent_back = True
generalbsdf.specular_intensity = 0.5
generalbsdf.use_backface_culling = False
generalbsdf.use_backface_culling_lightprobe_volume = True
generalbsdf.use_backface_culling_shadow = False
generalbsdf.use_preview_world = False
generalbsdf.use_raytrace_refraction = False
generalbsdf.use_screen_refraction = False
generalbsdf.use_sss_translucency = False
generalbsdf.use_thickness_from_shadow = False
generalbsdf.use_transparency_overlap = True
generalbsdf.use_transparent_shadow = True
generalbsdf.blend_method = 'HASHED'
generalbsdf.displacement_method = 'BUMP'
generalbsdf.preview_render_type = 'SPHERE'
generalbsdf.surface_render_method = 'DITHERED'
generalbsdf.thickness_mode = 'SPHERE'
generalbsdf.volume_intersection_method = 'FAST'
generalbsdf.specular_color = (1.0, 1.0, 1.0)
generalbsdf.diffuse_color = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
generalbsdf.line_color = (0.0, 0.0, 0.0, 0.0)

def shader_nodetree_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Shader Nodetree node group"""
    shader_nodetree = generalbsdf.node_tree

    # Start with a clean node tree
    for node in shader_nodetree.nodes:
        shader_nodetree.nodes.remove(node)
    shader_nodetree.color_tag = 'NONE'
    shader_nodetree.description = ""
    shader_nodetree.default_group_node_width = 140
    # Initialize shader_nodetree nodes

    # Node Principled BSDF
    principled_bsdf = shader_nodetree.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # Roughness
    principled_bsdf.inputs[2].default_value = 0.5
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    # Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    # Node Material Output
    material_output = shader_nodetree.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # Node Attribute
    attribute = shader_nodetree.nodes.new("ShaderNodeAttribute")
    attribute.name = "Attribute"
    attribute.attribute_name = "Object Colour"
    attribute.attribute_type = 'OBJECT'

    # Set locations
    shader_nodetree.nodes["Principled BSDF"].location = (0.0, 0.0)
    shader_nodetree.nodes["Material Output"].location = (400.67803955078125, -22.071231842041016)
    shader_nodetree.nodes["Attribute"].location = (-234.02667236328125, -22.316844940185547)

    # Set dimensions
    shader_nodetree.nodes["Principled BSDF"].width  = 240.0
    shader_nodetree.nodes["Principled BSDF"].height = 100.0

    shader_nodetree.nodes["Material Output"].width  = 140.0
    shader_nodetree.nodes["Material Output"].height = 100.0

    shader_nodetree.nodes["Attribute"].width  = 140.0
    shader_nodetree.nodes["Attribute"].height = 100.0


    # Initialize shader_nodetree links

    # principled_bsdf.BSDF -> material_output.Surface
    shader_nodetree.links.new(
        shader_nodetree.nodes["Principled BSDF"].outputs[0],
        shader_nodetree.nodes["Material Output"].inputs[0]
    )
    # attribute.Color -> principled_bsdf.Base Color
    shader_nodetree.links.new(
        shader_nodetree.nodes["Attribute"].outputs[0],
        shader_nodetree.nodes["Principled BSDF"].inputs[0]
    )

    return shader_nodetree


# Maps node tree creation functions to the node tree
# name, such that we don't recreate node trees unnecessarily
node_tree_names : dict[typing.Callable, str] = {}

shader_nodetree = shader_nodetree_node_group(node_tree_names)
node_tree_names[shader_nodetree_node_group] = shader_nodetree.name

