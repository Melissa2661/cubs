import bpy, mathutils


# initialize point_sampling node group
def point_sampling_node_group():
    point_sampling = bpy.data.node_groups.new(type='GeometryNodeTree', name="Point sampling")
    
    point_sampling.color_tag = 'NONE'
    point_sampling.description = ""
    
    # point_sampling interface
    # Socket Output
    output_socket = point_sampling.interface.new_socket(name="Output", in_out='OUTPUT',
                                                        socket_type='NodeSocketGeometry')
    output_socket.attribute_domain = 'POINT'
    
    # Socket Blue noise
    blue_noise_socket = point_sampling.interface.new_socket(name="Blue noise", in_out='INPUT',
                                                            socket_type='NodeSocketBool')
    blue_noise_socket.default_value = False
    blue_noise_socket.attribute_domain = 'POINT'
    
    # Socket Mesh
    mesh_socket = point_sampling.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'
    
    # Socket Density Max
    density_max_socket = point_sampling.interface.new_socket(name="Density Max", in_out='INPUT',
                                                             socket_type='NodeSocketFloat')
    density_max_socket.default_value = 100
    density_max_socket.min_value = 0.0
    density_max_socket.max_value = 3.4028234663852886e+38
    density_max_socket.subtype = 'NONE'
    density_max_socket.attribute_domain = 'POINT'
    
    # initialize point_sampling nodes
    # node Group Output
    group_output = point_sampling.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    
    # node Group Input
    group_input = point_sampling.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    
    # node Distribute Points on Faces
    distribute_points_on_faces = point_sampling.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces.name = "Distribute Points on Faces"
    distribute_points_on_faces.distribute_method = 'POISSON'
    distribute_points_on_faces.use_legacy_normal = False
    # Selection
    distribute_points_on_faces.inputs[1].default_value = True
    # Density Factor
    distribute_points_on_faces.inputs[5].default_value = 1.0
    # Seed
    distribute_points_on_faces.inputs[6].default_value = 6
    
    # node Math
    math = point_sampling.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'INVERSE_SQRT'
    math.use_clamp = False
    
    # node Sampling
    sampling = point_sampling.nodes.new("NodeFrame")
    sampling.label = "Poisson Disk Sampling"
    sampling.name = "Sampling"
    sampling.label_size = 20
    sampling.shrink = True
    
    # node Switch
    switch = point_sampling.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'
    
    # node White Noise (Random) Sampling
    white_noise__random__sampling = point_sampling.nodes.new("NodeFrame")
    white_noise__random__sampling.label = "Random Sampling"
    white_noise__random__sampling.name = "White Noise (Random) Sampling"
    white_noise__random__sampling.label_size = 20
    white_noise__random__sampling.shrink = True
    
    # node Reroute
    reroute = point_sampling.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    # node Reroute.001
    reroute_001 = point_sampling.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    # node Distribute Points on Faces.001
    distribute_points_on_faces_001 = point_sampling.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces_001.name = "Distribute Points on Faces.001"
    distribute_points_on_faces_001.distribute_method = 'RANDOM'
    distribute_points_on_faces_001.use_legacy_normal = False
    # Selection
    distribute_points_on_faces_001.inputs[1].default_value = True
    # Seed
    distribute_points_on_faces_001.inputs[6].default_value = 0
    
    # node Reroute.002
    reroute_002 = point_sampling.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    
    # Set parents
    distribute_points_on_faces.parent = sampling
    math.parent = sampling
    reroute.parent = sampling
    reroute_001.parent = sampling
    distribute_points_on_faces_001.parent = white_noise__random__sampling
    
    # Set locations
    group_output.location = (388.47412109375, 547.9915771484375)
    group_input.location = (-957.4458618164062, 520.0055541992188)
    distribute_points_on_faces.location = (315.568359375, 51.2125244140625)
    math.location = (77.404296875, -49.24711608886719)
    sampling.location = (-415.6026916503906, -32.0728759765625)
    switch.location = (207.03167724609375, 550.7303466796875)
    white_noise__random__sampling.location = (-429.8962707519531, 358.4704895019531)
    reroute.location = (6.781494140625, 73.88794708251953)
    reroute_001.location = (76.15103149414062, 102.61842346191406)
    distribute_points_on_faces_001.location = (173.14044189453125, 19.87408447265625)
    reroute_002.location = (-586.3506469726562, 210.3428192138672)
    
    # Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    distribute_points_on_faces.width, distribute_points_on_faces.height = 170.0, 100.0
    math.width, math.height = 140.0, 100.0
    sampling.width, sampling.height = 542.8211669921875, 379.5455322265625
    switch.width, switch.height = 140.0, 100.0
    white_noise__random__sampling.width, white_noise__random__sampling.height = 230.0, 280.0
    reroute.width, reroute.height = 16.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    distribute_points_on_faces_001.width, distribute_points_on_faces_001.height = 170.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    
    # initialize point_sampling links
    # distribute_points_on_faces.Points -> switch.True
    point_sampling.links.new(distribute_points_on_faces.outputs[0], switch.inputs[2])
    # math.Value -> distribute_points_on_faces.Distance Min
    point_sampling.links.new(math.outputs[0], distribute_points_on_faces.inputs[2])
    # reroute_001.Output -> distribute_points_on_faces.Mesh
    point_sampling.links.new(reroute_001.outputs[0], distribute_points_on_faces.inputs[0])
    # group_input.Blue noise -> switch.Switch
    point_sampling.links.new(group_input.outputs[0], switch.inputs[0])
    # reroute.Output -> distribute_points_on_faces.Density Max
    point_sampling.links.new(reroute.outputs[0], distribute_points_on_faces.inputs[3])
    # reroute.Output -> math.Value
    point_sampling.links.new(reroute.outputs[0], math.inputs[0])
    # switch.Output -> group_output.Output
    point_sampling.links.new(switch.outputs[0], group_output.inputs[0])
    # reroute_002.Output -> reroute.Input
    point_sampling.links.new(reroute_002.outputs[0], reroute.inputs[0])
    # group_input.Mesh -> reroute_001.Input
    point_sampling.links.new(group_input.outputs[1], reroute_001.inputs[0])
    # reroute_001.Output -> distribute_points_on_faces_001.Mesh
    point_sampling.links.new(reroute_001.outputs[0], distribute_points_on_faces_001.inputs[0])
    # distribute_points_on_faces_001.Points -> switch.False
    point_sampling.links.new(distribute_points_on_faces_001.outputs[0], switch.inputs[1])
    # reroute_002.Output -> distribute_points_on_faces_001.Density
    point_sampling.links.new(reroute_002.outputs[0], distribute_points_on_faces_001.inputs[4])
    # group_input.Density Max -> reroute_002.Input
    point_sampling.links.new(group_input.outputs[2], reroute_002.inputs[0])
    return point_sampling


point_sampling = point_sampling_node_group()


# initialize point_to_sphere node group
def point_to_sphere_node_group():
    point_to_sphere = bpy.data.node_groups.new(type='GeometryNodeTree', name="Point to Sphere")
    
    point_to_sphere.color_tag = 'NONE'
    point_to_sphere.description = ""
    
    # point_to_sphere interface
    # Socket Instances
    instances_socket = point_to_sphere.interface.new_socket(name="Instances", in_out='OUTPUT',
                                                            socket_type='NodeSocketGeometry')
    instances_socket.attribute_domain = 'POINT'
    
    # Socket Points
    points_socket = point_to_sphere.interface.new_socket(name="Points", in_out='INPUT',
                                                         socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    
    # Socket Sphere Radius
    sphere_radius_socket = point_to_sphere.interface.new_socket(name="Sphere Radius", in_out='INPUT',
                                                                socket_type='NodeSocketFloat')
    sphere_radius_socket.default_value = 0.029999999329447746
    sphere_radius_socket.min_value = 0.0
    sphere_radius_socket.max_value = 3.4028234663852886e+38
    sphere_radius_socket.subtype = 'DISTANCE'
    sphere_radius_socket.default_attribute_name = "0.01"
    sphere_radius_socket.attribute_domain = 'POINT'
    sphere_radius_socket.description = "Radius of the sphere that will be rendered"
    
    # initialize point_to_sphere nodes
    # node Group Output
    group_output_1 = point_to_sphere.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    
    # node Group Input
    group_input_1 = point_to_sphere.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    
    # node Instance on Points
    instance_on_points = point_to_sphere.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    # Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
    
    # node Ico Sphere
    ico_sphere = point_to_sphere.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    # Subdivisions
    ico_sphere.inputs[1].default_value = 3
    
    # node Set Shade Smooth
    set_shade_smooth = point_to_sphere.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True
    
    # Set locations
    group_output_1.location = (361.3283386230469, 110.83648681640625)
    group_input_1.location = (-439.05426025390625, 0.9823775887489319)
    instance_on_points.location = (182.13006591796875, 112.15104675292969)
    ico_sphere.location = (-239.05426025390625, -110.00904846191406)
    set_shade_smooth.location = (-39.45298767089844, -11.948493957519531)
    
    # Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    ico_sphere.width, ico_sphere.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    
    # initialize point_to_sphere links
    # ico_sphere.Mesh -> set_shade_smooth.Geometry
    point_to_sphere.links.new(ico_sphere.outputs[0], set_shade_smooth.inputs[0])
    # set_shade_smooth.Geometry -> instance_on_points.Instance
    point_to_sphere.links.new(set_shade_smooth.outputs[0], instance_on_points.inputs[2])
    # group_input_1.Points -> instance_on_points.Points
    point_to_sphere.links.new(group_input_1.outputs[0], instance_on_points.inputs[0])
    # instance_on_points.Instances -> group_output_1.Instances
    point_to_sphere.links.new(instance_on_points.outputs[0], group_output_1.inputs[0])
    # group_input_1.Sphere Radius -> ico_sphere.Radius
    point_to_sphere.links.new(group_input_1.outputs[1], ico_sphere.inputs[0])
    return point_to_sphere


point_to_sphere = point_to_sphere_node_group()


# initialize sample_points_from_mesh node group
def sample_points_from_mesh_node_group():
    sample_points_from_mesh = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sample Points from Mesh")
    
    sample_points_from_mesh.color_tag = 'NONE'
    sample_points_from_mesh.description = ""
    
    sample_points_from_mesh.is_modifier = True
    
    # sample_points_from_mesh interface
    # Socket Geometry
    geometry_socket = sample_points_from_mesh.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                                   socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    
    # Socket Geometry
    geometry_socket_1 = sample_points_from_mesh.interface.new_socket(name="Geometry", in_out='INPUT',
                                                                     socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    
    # Socket Blue noise
    blue_noise_socket_1 = sample_points_from_mesh.interface.new_socket(name="Blue noise", in_out='INPUT',
                                                                       socket_type='NodeSocketBool')
    blue_noise_socket_1.default_value = False
    blue_noise_socket_1.attribute_domain = 'POINT'
    blue_noise_socket_1.description = "Use blue noise (poisson disk) sampling if True, white noise (random) sampling if False."
    
    # Socket Max Density
    max_density_socket = sample_points_from_mesh.interface.new_socket(name="Max Density", in_out='INPUT',
                                                                      socket_type='NodeSocketFloat')
    max_density_socket.default_value = 100.0
    max_density_socket.min_value = 0.0
    max_density_socket.max_value = 3.4028234663852886e+38
    max_density_socket.subtype = 'NONE'
    max_density_socket.attribute_domain = 'POINT'
    
    # Socket Material
    material_socket = sample_points_from_mesh.interface.new_socket(name="Material", in_out='INPUT',
                                                                   socket_type='NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    
    # initialize sample_points_from_mesh nodes
    # node Group Input
    group_input_2 = sample_points_from_mesh.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    
    # node Group Output
    group_output_2 = sample_points_from_mesh.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    
    # node Join Geometry
    join_geometry = sample_points_from_mesh.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    
    # node Set Material
    set_material = sample_points_from_mesh.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True
    
    # node Group
    group = sample_points_from_mesh.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = point_sampling
    
    # node Reroute
    reroute_1 = sample_points_from_mesh.nodes.new("NodeReroute")
    reroute_1.name = "Reroute"
    # node Group.001
    group_001 = sample_points_from_mesh.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = point_to_sphere
    # Socket_2
    group_001.inputs[1].default_value = 0.029999999329447746
    
    # node Reroute.001
    reroute_001_1 = sample_points_from_mesh.nodes.new("NodeReroute")
    reroute_001_1.name = "Reroute.001"
    
    # Set locations
    group_input_2.location = (-878.5484619140625, 385.6933288574219)
    group_output_2.location = (455.7042541503906, 303.553466796875)
    join_geometry.location = (223.66485595703125, 302.2284240722656)
    set_material.location = (28.977262496948242, 163.10450744628906)
    group.location = (-420.3677673339844, 245.21676635742188)
    reroute_1.location = (-521.6708984375, 345.2888488769531)
    group_001.location = (-235.830078125, 241.42465209960938)
    reroute_001_1.location = (-423.37322998046875, 58.64510726928711)
    
    # Set dimensions
    group_input_2.width, group_input_2.height = 140.0, 100.0
    group_output_2.width, group_output_2.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    reroute_1.width, reroute_1.height = 16.0, 100.0
    group_001.width, group_001.height = 181.29412841796875, 100.0
    reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
    
    # initialize sample_points_from_mesh links
    # join_geometry.Geometry -> group_output_2.Geometry
    sample_points_from_mesh.links.new(join_geometry.outputs[0], group_output_2.inputs[0])
    # set_material.Geometry -> join_geometry.Geometry
    sample_points_from_mesh.links.new(set_material.outputs[0], join_geometry.inputs[0])
    # group_001.Instances -> set_material.Geometry
    sample_points_from_mesh.links.new(group_001.outputs[0], set_material.inputs[0])
    # reroute_1.Output -> group.Mesh
    sample_points_from_mesh.links.new(reroute_1.outputs[0], group.inputs[1])
    # group_input_2.Blue noise -> group.Blue noise
    sample_points_from_mesh.links.new(group_input_2.outputs[1], group.inputs[0])
    # group_input_2.Max Density -> group.Density Max
    sample_points_from_mesh.links.new(group_input_2.outputs[2], group.inputs[2])
    # group_input_2.Geometry -> reroute_1.Input
    sample_points_from_mesh.links.new(group_input_2.outputs[0], reroute_1.inputs[0])
    # group.Output -> group_001.Points
    sample_points_from_mesh.links.new(group.outputs[0], group_001.inputs[0])
    # reroute_001_1.Output -> set_material.Material
    sample_points_from_mesh.links.new(reroute_001_1.outputs[0], set_material.inputs[2])
    # group_input_2.Material -> reroute_001_1.Input
    sample_points_from_mesh.links.new(group_input_2.outputs[3], reroute_001_1.inputs[0])
    # reroute_1.Output -> join_geometry.Geometry
    sample_points_from_mesh.links.new(reroute_1.outputs[0], join_geometry.inputs[0])
    return sample_points_from_mesh


sample_points_from_mesh = sample_points_from_mesh_node_group()

