import bpy
import mathutils
import os
import typing

# NOTE: you must first load the images used for the enviroment map:
# for options in ["city.exr", "interior.exr", "forest.exr"]:
#     env_light_path = bpy.context.preferences.studio_lights[options].path
#     im = bpy.data.images.load(env_light_path, check_existing=True)
# from shader_nodes import world_environment_map
# ...


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
    background.inputs[1].default_value = 0.4

    # Node Environment Texture
    environment_texture = shader_nodetree.nodes.new("ShaderNodeTexEnvironment")
    environment_texture.name = "Environment Texture"
    if "interior.exr" in bpy.data.images:
        environment_texture.image = bpy.data.images["interior.exr"]
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
    if "city.exr" in bpy.data.images:
        environment_texture_001.image = bpy.data.images["city.exr"]
    environment_texture_001.image_user.frame_current = 0
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
    if "forest.exr" in bpy.data.images:
        environment_texture_002.image = bpy.data.images["forest.exr"]
    environment_texture_002.image_user.frame_current = 0
    environment_texture_002.image_user.frame_duration = 100
    environment_texture_002.image_user.frame_offset = 0
    environment_texture_002.image_user.frame_start = 1
    environment_texture_002.image_user.tile = 0
    environment_texture_002.image_user.use_auto_refresh = False
    environment_texture_002.image_user.use_cyclic = False
    environment_texture_002.interpolation = 'Linear'
    environment_texture_002.projection = 'EQUIRECTANGULAR'
    # Vector
    environment_texture_002.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Set locations
    shader_nodetree.nodes["World Output"].location = (300.0, 300.0)
    shader_nodetree.nodes["Background"].location = (10.0, 300.0)
    shader_nodetree.nodes["Environment Texture"].location = (-317.1870422363281, 300.22479248046875)
    shader_nodetree.nodes["Environment Texture.001"].location = (-323.61712646484375, 49.560142517089844)
    shader_nodetree.nodes["Environment Texture.002"].location = (-317.9209899902344, 545.8694458007812)

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


    # Initialize shader_nodetree links

    # background.Background -> world_output.Surface
    shader_nodetree.links.new(
        shader_nodetree.nodes["Background"].outputs[0],
        shader_nodetree.nodes["World Output"].inputs[0]
    )
    # environment_texture_001.Color -> background.Color
    shader_nodetree.links.new(
        shader_nodetree.nodes["Environment Texture.001"].outputs[0],
        shader_nodetree.nodes["Background"].inputs[0]
    )

    return shader_nodetree


# Maps node tree creation functions to the node tree
# name, such that we don't recreate node trees unnecessarily
node_tree_names : dict[typing.Callable, str] = {}

shader_nodetree = shader_nodetree_node_group(node_tree_names)
node_tree_names[shader_nodetree_node_group] = shader_nodetree.name

