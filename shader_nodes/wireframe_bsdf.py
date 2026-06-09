import bpy
import mathutils
import os
import typing


generalwireframe = bpy.data.materials.new(name="GeneralWireframe")
if bpy.app.version < (5, 0, 0):
    generalwireframe.use_nodes = True


generalwireframe.alpha_threshold = 0.5
generalwireframe.line_priority = 0
generalwireframe.max_vertex_displacement = 0.0
generalwireframe.metallic = 0.0
generalwireframe.paint_active_slot = 0
generalwireframe.paint_clone_slot = 0
generalwireframe.pass_index = 0
generalwireframe.refraction_depth = 0.0
generalwireframe.roughness = 0.4000000059604645
generalwireframe.show_transparent_back = True
generalwireframe.specular_intensity = 0.5
generalwireframe.use_backface_culling = False
generalwireframe.use_backface_culling_lightprobe_volume = True
generalwireframe.use_backface_culling_shadow = False
generalwireframe.use_preview_world = False
generalwireframe.use_raytrace_refraction = False
generalwireframe.use_screen_refraction = False
generalwireframe.use_sss_translucency = False
generalwireframe.use_thickness_from_shadow = False
generalwireframe.use_transparency_overlap = True
generalwireframe.use_transparent_shadow = True
generalwireframe.blend_method = 'HASHED'
generalwireframe.displacement_method = 'BUMP'
generalwireframe.preview_render_type = 'SPHERE'
generalwireframe.surface_render_method = 'DITHERED'
generalwireframe.thickness_mode = 'SPHERE'
generalwireframe.volume_intersection_method = 'FAST'
generalwireframe.specular_color = (1.0, 1.0, 1.0)
generalwireframe.diffuse_color = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
generalwireframe.line_color = (0.0, 0.0, 0.0, 0.0)


def shader_nodetree_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Shader Nodetree node group"""
    shader_nodetree = generalwireframe.node_tree

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

    # Node Mix Shader
    mix_shader = shader_nodetree.nodes.new("ShaderNodeMixShader")
    mix_shader.name = "Mix Shader"

    # Node Wireframe
    wireframe = shader_nodetree.nodes.new("ShaderNodeWireframe")
    wireframe.name = "Wireframe"
    wireframe.use_pixel_size = False

    # Node Attribute.001
    attribute_001 = shader_nodetree.nodes.new("ShaderNodeAttribute")
    attribute_001.name = "Attribute.001"
    attribute_001.attribute_name = "Wireframe Colour"
    attribute_001.attribute_type = 'OBJECT'

    # Node Attribute.002
    attribute_002 = shader_nodetree.nodes.new("ShaderNodeAttribute")
    attribute_002.name = "Attribute.002"
    attribute_002.attribute_name = "Wireframe Width"
    attribute_002.attribute_type = 'OBJECT'

    # Set locations
    shader_nodetree.nodes["Principled BSDF"].location = (-302.3709411621094, 196.155029296875)
    shader_nodetree.nodes["Material Output"].location = (209.4794158935547, 160.09588623046875)
    shader_nodetree.nodes["Attribute"].location = (-501.6885986328125, 108.07891845703125)
    shader_nodetree.nodes["Mix Shader"].location = (27.389739990234375, 134.69512939453125)
    shader_nodetree.nodes["Wireframe"].location = (-205.21194458007812, 320.72509765625)
    shader_nodetree.nodes["Attribute.001"].location = (-206.47927856445312, -162.7932891845703)
    shader_nodetree.nodes["Attribute.002"].location = (-501.8770751953125, 315.1289367675781)

    # Set dimensions
    shader_nodetree.nodes["Principled BSDF"].width  = 240.0
    shader_nodetree.nodes["Principled BSDF"].height = 100.0

    shader_nodetree.nodes["Material Output"].width  = 140.0
    shader_nodetree.nodes["Material Output"].height = 100.0

    shader_nodetree.nodes["Attribute"].width  = 140.0
    shader_nodetree.nodes["Attribute"].height = 100.0

    shader_nodetree.nodes["Mix Shader"].width  = 140.0
    shader_nodetree.nodes["Mix Shader"].height = 100.0

    shader_nodetree.nodes["Wireframe"].width  = 140.0
    shader_nodetree.nodes["Wireframe"].height = 100.0

    shader_nodetree.nodes["Attribute.001"].width  = 140.0
    shader_nodetree.nodes["Attribute.001"].height = 100.0

    shader_nodetree.nodes["Attribute.002"].width  = 140.0
    shader_nodetree.nodes["Attribute.002"].height = 100.0


    # Initialize shader_nodetree links

    # attribute.Color -> principled_bsdf.Base Color
    shader_nodetree.links.new(
        shader_nodetree.nodes["Attribute"].outputs[0],
        shader_nodetree.nodes["Principled BSDF"].inputs[0]
    )
    # principled_bsdf.BSDF -> mix_shader.Shader
    shader_nodetree.links.new(
        shader_nodetree.nodes["Principled BSDF"].outputs[0],
        shader_nodetree.nodes["Mix Shader"].inputs[1]
    )
    # attribute_001.Color -> mix_shader.Shader
    shader_nodetree.links.new(
        shader_nodetree.nodes["Attribute.001"].outputs[0],
        shader_nodetree.nodes["Mix Shader"].inputs[2]
    )
    # attribute_002.Fac -> wireframe.Size
    shader_nodetree.links.new(
        shader_nodetree.nodes["Attribute.002"].outputs[2],
        shader_nodetree.nodes["Wireframe"].inputs[0]
    )
    # mix_shader.Shader -> material_output.Surface
    shader_nodetree.links.new(
        shader_nodetree.nodes["Mix Shader"].outputs[0],
        shader_nodetree.nodes["Material Output"].inputs[0]
    )
    # wireframe.Fac -> mix_shader.Fac
    shader_nodetree.links.new(
        shader_nodetree.nodes["Wireframe"].outputs[0],
        shader_nodetree.nodes["Mix Shader"].inputs[0]
    )

    return shader_nodetree


# Maps node tree creation functions to the node tree
# name, such that we don't recreate node trees unnecessarily
node_tree_names : dict[typing.Callable, str] = {}

shader_nodetree = shader_nodetree_node_group(node_tree_names)
node_tree_names[shader_nodetree_node_group] = shader_nodetree.name

