import bpy

context = bpy.context
scene = bpy.data.scenes["Scene"]
render = scene.render

render.engine = 'CYCLES'  # ('BLENDER_EEVEE_NEXT', 'BLENDER_WORKBENCH', 'CYCLES')
render.image_settings.color_mode = 'RGBA'  # ('RGB', 'RGBA', ...)
render.image_settings.color_depth = '8'  # ('8', '16')
render.image_settings.file_format = 'PNG'  # ('PNG', 'OPEN_EXR', 'JPEG, ...)
render.image_settings.compression = 50
# Change resolution as required
render.resolution_x = 1920
render.resolution_y = 1080
render.film_transparent = True
render.use_persistent_data = True

scene.display_settings.display_device = "sRGB"
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "Very High Contrast"

scene.cycles.preview_samples = 32
scene.cycles.samples = 100
scene.cycles.device = 'GPU'
scene.cycles.use_denoising = True
scene.cycles.transparent_max_bounces = 9

# Create Compositor nodes so that our final output does not produce shadows on the entire image
# Inspired by Silvia Sellán's solution found here: https://www.silviasellan.com/posts/blender_figure/

# Make sure the Compositor actually uses nodes
scene.use_nodes = True
ntree = scene.node_tree
# Two nodes are already initialized by default
ntree_in = ntree.nodes['Render Layers']
ntree_out = ntree.nodes['Composite']
ntree_out.location = (850, 40)
ntree.links.new(ntree_in.outputs['Image'], ntree_out.inputs['Image'])

# Create colour ramp to get rid of subtle shadows
ramp = ntree.nodes.new("CompositorNodeValToRGB")
ramp.location = (350, -100)
ramp_start = ramp.color_ramp.elements[0]
ramp_end = ramp.color_ramp.elements[1]
ramp_start.position = 0.1
ramp_start.color = (0, 0, 0, 0)
ramp_end.color = (0, 0, 0, 1)
ntree.links.new(ntree_in.outputs['Alpha'], ramp.inputs['Fac'])
ntree.links.new(ramp.outputs['Alpha'], ntree_out.inputs['Alpha'])

# Modify image brightness
bright = ntree.nodes.new("CompositorNodeBrightContrast")
bright.location = (350, 130)
bright.use_premultiply = False

# Modify image gamma
gamma = ntree.nodes.new("CompositorNodeGamma")
gamma.location = (550, 130)
ntree.links.new(ntree_in.outputs['Image'], bright.inputs['Image'])
ntree.links.new(bright.outputs['Image'], gamma.inputs['Image'])
ntree.links.new(gamma.outputs['Image'], ntree_out.inputs['Image'])

