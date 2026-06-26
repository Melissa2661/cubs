import bpy
import mathutils
import os
import typing


# NOTE: you must load the images used for the enviroment map in your code BEFORE importing this file:
# for option in ["city.exr", "courtyard.exr", "forest.exr", "interior.exr", "night.exr", "studio.exr", "sunrise.exr", "sunset.exr"]:
#     env_light_path = bpy.context.preferences.studio_lights[option].path
#     im = bpy.data.images.load(env_light_path, check_existing=True)

world = bpy.data.worlds["World"]
if bpy.app.version < (5, 0, 0):
    world.use_nodes = True


world.sun_angle = 0.009180432185530663
world.sun_shadow_filter_radius = 1.0
world.sun_shadow_jitter_overblur = 0.0
world.sun_shadow_maximum_resolution = 0.0010000000474974513
world.sun_threshold = 10.0
world.use_eevee_finite_volume = False
world.use_sun_shadow = True
world.use_sun_shadow_jitter = False
world.probe_resolution = '1024'
world.color = (0.05087608844041824, 0.05087608844041824, 0.05087608844041824)
world.lightgroup = ""

def shader_nodetree_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Shader Nodetree node group"""
    shader_nodetree = world.node_tree

    # Start with a clean node tree
    for node in shader_nodetree.nodes:
        shader_nodetree.nodes.remove(node)
    shader_nodetree.color_tag = 'NONE'
    shader_nodetree.description = ""
    shader_nodetree.default_group_node_width = 140
    # Initialize shader_nodetree nodes

    # Node World Output
    world_output = shader_nodetree.nodes.new("ShaderNodeOutputWorld")
    world_output.name = "World Output"
    world_output.is_active_output = True
    world_output.target = 'ALL'

    # Node Background
    background = shader_nodetree.nodes.new("ShaderNodeBackground")
    background.name = "Background"
    # Strength
    background.inputs[1].default_value = 0.30000001192092896

    # Node Environment Texture
    environment_texture = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture.name = "Environment Texture"
    if "courtyard.exr" in bpy.data.images:
        environment_texture.image = bpy.data.images["courtyard.exr"]
    environment_texture.image_user.frame_current = 1
    environment_texture.image_user.frame_duration = 1
    environment_texture.image_user.frame_offset = -1
    environment_texture.image_user.frame_start = 1
    environment_texture.image_user.tile = 0
    environment_texture.image_user.use_auto_refresh = False
    environment_texture.image_user.use_cyclic = False
    environment_texture.interpolation = 'Linear'
    environment_texture.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.001
    environment_texture_001 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_001.name = "Environment Texture.001"
    if "forest.exr" in bpy.data.images:
        environment_texture_001.image = bpy.data.images["forest.exr"]
    environment_texture_001.image_user.frame_current = 1
    environment_texture_001.image_user.frame_duration = 1
    environment_texture_001.image_user.frame_offset = -1
    environment_texture_001.image_user.frame_start = 1
    environment_texture_001.image_user.tile = 0
    environment_texture_001.image_user.use_auto_refresh = False
    environment_texture_001.image_user.use_cyclic = False
    environment_texture_001.interpolation = 'Linear'
    environment_texture_001.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.002
    environment_texture_002 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_002.name = "Environment Texture.002"
    if "city.exr" in bpy.data.images:
        environment_texture_002.image = bpy.data.images["city.exr"]
    environment_texture_002.image_user.frame_current = 1
    environment_texture_002.image_user.frame_duration = 1
    environment_texture_002.image_user.frame_offset = -1
    environment_texture_002.image_user.frame_start = 1
    environment_texture_002.image_user.tile = 0
    environment_texture_002.image_user.use_auto_refresh = False
    environment_texture_002.image_user.use_cyclic = False
    environment_texture_002.interpolation = 'Linear'
    environment_texture_002.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_002.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.003
    environment_texture_003 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_003.name = "Environment Texture.003"
    if "interior.exr" in bpy.data.images:
        environment_texture_003.image = bpy.data.images["interior.exr"]
    environment_texture_003.image_user.frame_current = 1
    environment_texture_003.image_user.frame_duration = 1
    environment_texture_003.image_user.frame_offset = -1
    environment_texture_003.image_user.frame_start = 1
    environment_texture_003.image_user.tile = 0
    environment_texture_003.image_user.use_auto_refresh = False
    environment_texture_003.image_user.use_cyclic = False
    environment_texture_003.interpolation = 'Linear'
    environment_texture_003.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_003.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.004
    environment_texture_004 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_004.name = "Environment Texture.004"
    if "night.exr" in bpy.data.images:
        environment_texture_004.image = bpy.data.images["night.exr"]
    environment_texture_004.image_user.frame_current = 1
    environment_texture_004.image_user.frame_duration = 1
    environment_texture_004.image_user.frame_offset = -1
    environment_texture_004.image_user.frame_start = 1
    environment_texture_004.image_user.tile = 0
    environment_texture_004.image_user.use_auto_refresh = False
    environment_texture_004.image_user.use_cyclic = False
    environment_texture_004.interpolation = 'Linear'
    environment_texture_004.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_004.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.005
    environment_texture_005 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_005.name = "Environment Texture.005"
    if "studio.exr" in bpy.data.images:
        environment_texture_005.image = bpy.data.images["studio.exr"]
    environment_texture_005.image_user.frame_current = 1
    environment_texture_005.image_user.frame_duration = 1
    environment_texture_005.image_user.frame_offset = -1
    environment_texture_005.image_user.frame_start = 1
    environment_texture_005.image_user.tile = 0
    environment_texture_005.image_user.use_auto_refresh = False
    environment_texture_005.image_user.use_cyclic = False
    environment_texture_005.interpolation = 'Linear'
    environment_texture_005.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_005.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.006
    environment_texture_006 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_006.name = "Environment Texture.006"
    if "sunrise.exr" in bpy.data.images:
        environment_texture_006.image = bpy.data.images["sunrise.exr"]
    environment_texture_006.image_user.frame_current = 1
    environment_texture_006.image_user.frame_duration = 1
    environment_texture_006.image_user.frame_offset = -1
    environment_texture_006.image_user.frame_start = 1
    environment_texture_006.image_user.tile = 0
    environment_texture_006.image_user.use_auto_refresh = False
    environment_texture_006.image_user.use_cyclic = False
    environment_texture_006.interpolation = 'Linear'
    environment_texture_006.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_006.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Environment Texture.007
    environment_texture_007 = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture_007.name = "Environment Texture.007"
    if "sunset.exr.001" in bpy.data.images:
        environment_texture_007.image = bpy.data.images["sunset.exr.001"]
    environment_texture_007.image_user.frame_current = 1
    environment_texture_007.image_user.frame_duration = 1
    environment_texture_007.image_user.frame_offset = -1
    environment_texture_007.image_user.frame_start = 1
    environment_texture_007.image_user.tile = 0
    environment_texture_007.image_user.use_auto_refresh = False
    environment_texture_007.image_user.use_cyclic = False
    environment_texture_007.interpolation = 'Linear'
    environment_texture_007.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_007.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Set locations
    shader_nodetree.nodes["World Output"].location = (282.2548828125, 355.6393127441406)
    shader_nodetree.nodes["Background"].location = (-7.7451171875, 355.6393127441406)
    shader_nodetree.nodes["Environment Texture"].location = (-334.9321594238281, 355.8641052246094)
    shader_nodetree.nodes["Environment Texture.001"].location = (-332.60797119140625, 105.19945526123047)
    shader_nodetree.nodes["Environment Texture.002"].location = (-335.6661071777344, 601.5087890625)
    shader_nodetree.nodes["Environment Texture.003"].location = (-609.8135375976562, 606.7267456054688)
    shader_nodetree.nodes["Environment Texture.004"].location = (-606.4789428710938, 356.0068359375)
    shader_nodetree.nodes["Environment Texture.005"].location = (-607.5599365234375, 108.62222290039062)
    shader_nodetree.nodes["Environment Texture.006"].location = (-871.62451171875, 431.4305419921875)
    shader_nodetree.nodes["Environment Texture.007"].location = (-871.5357055664062, 189.13282775878906)

    # Set dimensions
    shader_nodetree.nodes["World Output"].width  = 140.0
    shader_nodetree.nodes["World Output"].height = 100.0

    shader_nodetree.nodes["Background"].width  = 140.0
    shader_nodetree.nodes["Background"].height = 100.0

    shader_nodetree.nodes["Environment Texture"].width  = 240.0
    shader_nodetree.nodes["Environment Texture"].height = 100.0

    shader_nodetree.nodes["Environment Texture.001"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.001"].height = 100.0

    shader_nodetree.nodes["Environment Texture.002"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.002"].height = 100.0

    shader_nodetree.nodes["Environment Texture.003"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.003"].height = 100.0

    shader_nodetree.nodes["Environment Texture.004"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.004"].height = 100.0

    shader_nodetree.nodes["Environment Texture.005"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.005"].height = 100.0

    shader_nodetree.nodes["Environment Texture.006"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.006"].height = 100.0

    shader_nodetree.nodes["Environment Texture.007"].width  = 240.0
    shader_nodetree.nodes["Environment Texture.007"].height = 100.0


    # Initialize shader_nodetree links

    # background.Background -> world_output.Surface
    shader_nodetree.links.new(
        shader_nodetree.nodes["Background"].outputs[0],
        shader_nodetree.nodes["World Output"].inputs[0]
    )
    # environment_texture_002.Color -> background.Color
    shader_nodetree.links.new(
        shader_nodetree.nodes["Environment Texture.002"].outputs[0],
        shader_nodetree.nodes["Background"].inputs[0]
    )

    return shader_nodetree


# Maps node tree creation functions to the node tree
# name, such that we don't recreate node trees unnecessarily
node_tree_names : dict[typing.Callable, str] = {}

shader_nodetree = shader_nodetree_node_group(node_tree_names)
node_tree_names[shader_nodetree_node_group] = shader_nodetree.name

