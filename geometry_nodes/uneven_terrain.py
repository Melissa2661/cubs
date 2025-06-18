import bpy, mathutils


# initialize uneven_terrain node group
def uneven_terrain_node_group():
    uneven_terrain = bpy.data.node_groups.new(type='GeometryNodeTree', name="Uneven Terrain")
    
    uneven_terrain.color_tag = 'NONE'
    uneven_terrain.description = ""
    
    uneven_terrain.is_modifier = True
    
    # uneven_terrain interface
    # Socket Geometry
    geometry_socket = uneven_terrain.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                          socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    
    # Socket Geometry
    geometry_socket_1 = uneven_terrain.interface.new_socket(name="Geometry", in_out='INPUT',
                                                            socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    
    # initialize uneven_terrain nodes
    # node Group Input
    group_input = uneven_terrain.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    
    # node Group Output
    group_output = uneven_terrain.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    
    # node Instance on Points
    instance_on_points = uneven_terrain.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    
    # node Ico Sphere
    ico_sphere = uneven_terrain.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    # Radius
    ico_sphere.inputs[0].default_value = 1.0
    # Subdivisions
    ico_sphere.inputs[1].default_value = 3
    
    # node Set Position
    set_position = uneven_terrain.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)
    
    # node Noise Texture
    noise_texture = uneven_terrain.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture.inputs[2].default_value = 5.0
    # Detail
    noise_texture.inputs[3].default_value = 2.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0
    
    # node Combine XYZ
    combine_xyz = uneven_terrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Z
    combine_xyz.inputs[2].default_value = 0.0
    
    # node Map Range
    map_range = uneven_terrain.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    # From Min
    map_range.inputs[1].default_value = 0.0
    # From Max
    map_range.inputs[2].default_value = 1.0
    # To Min
    map_range.inputs[3].default_value = -0.10000000149011612
    # To Max
    map_range.inputs[4].default_value = 0.10000000149011612
    
    # node Noise Texture.001
    noise_texture_001 = uneven_terrain.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'HETERO_TERRAIN'
    noise_texture_001.normalize = True
    # Vector
    noise_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture_001.inputs[2].default_value = 21.499998092651367
    # Detail
    noise_texture_001.inputs[3].default_value = 2.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Offset
    noise_texture_001.inputs[6].default_value = 0.29999998211860657
    # Distortion
    noise_texture_001.inputs[8].default_value = 6.999999523162842
    
    # node Map Range.001
    map_range_001 = uneven_terrain.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    # From Min
    map_range_001.inputs[1].default_value = 0.0
    # From Max
    map_range_001.inputs[2].default_value = 1.0
    # To Min
    map_range_001.inputs[3].default_value = 0.05000000074505806
    # To Max
    map_range_001.inputs[4].default_value = 0.10000000149011612
    
    # node Combine XYZ.001
    combine_xyz_001 = uneven_terrain.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    
    # Set locations
    group_input.location = (-618.944091796875, 19.642520904541016)
    group_output.location = (204.70489501953125, 93.05830383300781)
    instance_on_points.location = (-27.475173950195312, 9.975112915039062)
    ico_sphere.location = (-390.1331481933594, -141.74285888671875)
    set_position.location = (-376.7615966796875, 43.89533996582031)
    noise_texture.location = (-1005.4406127929688, -57.362579345703125)
    combine_xyz.location = (-616.8931884765625, -92.31636047363281)
    map_range.location = (-822.3896484375, -67.37181854248047)
    noise_texture_001.location = (-1009.7078857421875, -362.7899475097656)
    map_range_001.location = (-685.3841552734375, -399.2589111328125)
    combine_xyz_001.location = (-457.6827697753906, -394.1141662597656)
    
    # Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    ico_sphere.width, ico_sphere.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    map_range_001.width, map_range_001.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    
    # initialize uneven_terrain links
    # set_position.Geometry -> instance_on_points.Points
    uneven_terrain.links.new(set_position.outputs[0], instance_on_points.inputs[0])
    # ico_sphere.Mesh -> instance_on_points.Instance
    uneven_terrain.links.new(ico_sphere.outputs[0], instance_on_points.inputs[2])
    # group_input.Geometry -> set_position.Geometry
    uneven_terrain.links.new(group_input.outputs[0], set_position.inputs[0])
    # noise_texture.Fac -> map_range.Value
    uneven_terrain.links.new(noise_texture.outputs[0], map_range.inputs[0])
    # map_range.Result -> combine_xyz.Y
    uneven_terrain.links.new(map_range.outputs[0], combine_xyz.inputs[1])
    # instance_on_points.Instances -> group_output.Geometry
    uneven_terrain.links.new(instance_on_points.outputs[0], group_output.inputs[0])
    # noise_texture_001.Fac -> map_range_001.Value
    uneven_terrain.links.new(noise_texture_001.outputs[0], map_range_001.inputs[0])
    # noise_texture_001.Fac -> map_range_001.Vector
    uneven_terrain.links.new(noise_texture_001.outputs[0], map_range_001.inputs[6])
    # map_range_001.Result -> combine_xyz_001.X
    uneven_terrain.links.new(map_range_001.outputs[0], combine_xyz_001.inputs[0])
    # map_range_001.Result -> combine_xyz_001.Y
    uneven_terrain.links.new(map_range_001.outputs[0], combine_xyz_001.inputs[1])
    # map_range_001.Result -> combine_xyz_001.Z
    uneven_terrain.links.new(map_range_001.outputs[0], combine_xyz_001.inputs[2])
    # combine_xyz.Vector -> set_position.Offset
    uneven_terrain.links.new(combine_xyz.outputs[0], set_position.inputs[3])
    # combine_xyz_001.Vector -> instance_on_points.Scale
    uneven_terrain.links.new(combine_xyz_001.outputs[0], instance_on_points.inputs[6])
    return uneven_terrain


terrain = uneven_terrain_node_group()

