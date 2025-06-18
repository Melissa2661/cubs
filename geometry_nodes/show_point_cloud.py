import bpy, mathutils


# initialize show_point_cloud node group
def show_point_cloud_node_group():
    show_point_cloud = bpy.data.node_groups.new(type='GeometryNodeTree', name="Show Point Cloud")
    
    show_point_cloud.color_tag = 'NONE'
    show_point_cloud.description = ""
    
    show_point_cloud.is_modifier = True
    
    # show_point_cloud interface
    # Socket Geometry
    geometry_socket = show_point_cloud.interface.new_socket(name="Geometry", in_out='OUTPUT',
                                                            socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    
    # Socket Geometry
    geometry_socket_1 = show_point_cloud.interface.new_socket(name="Geometry", in_out='INPUT',
                                                              socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    
    # Socket Point Material
    point_material_socket = show_point_cloud.interface.new_socket(name="Point Material", in_out='INPUT',
                                                                  socket_type='NodeSocketMaterial')
    point_material_socket.attribute_domain = 'POINT'
    point_material_socket.description = "Material"
    
    # initialize show_point_cloud nodes
    # node Group Input
    group_input = show_point_cloud.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    
    # node Group Output
    group_output = show_point_cloud.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    
    # node Ico Sphere
    ico_sphere = show_point_cloud.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    # Radius
    ico_sphere.inputs[0].default_value = 0.029999999329447746
    # Subdivisions
    ico_sphere.inputs[1].default_value = 3
    
    # node Instance on Points
    instance_on_points = show_point_cloud.nodes.new("GeometryNodeInstanceOnPoints")
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
    
    # node Set Material
    set_material = show_point_cloud.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True
    
    # Set locations
    group_input.location = (-268.26055908203125, 95.55316162109375)
    group_output.location = (375.13677978515625, 141.91465759277344)
    ico_sphere.location = (-266.979736328125, -18.648399353027344)
    instance_on_points.location = (-59.0997314453125, 4.5728759765625)
    set_material.location = (176.37425231933594, 141.4355926513672)
    
    # Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    ico_sphere.width, ico_sphere.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    
    # initialize show_point_cloud links
    # group_input.Geometry -> instance_on_points.Points
    show_point_cloud.links.new(group_input.outputs[0], instance_on_points.inputs[0])
    # ico_sphere.Mesh -> instance_on_points.Instance
    show_point_cloud.links.new(ico_sphere.outputs[0], instance_on_points.inputs[2])
    # group_input.Point Material -> set_material.Material
    show_point_cloud.links.new(group_input.outputs[1], set_material.inputs[2])
    # set_material.Geometry -> group_output.Geometry
    show_point_cloud.links.new(set_material.outputs[0], group_output.inputs[0])
    # instance_on_points.Instances -> set_material.Geometry
    show_point_cloud.links.new(instance_on_points.outputs[0], set_material.inputs[0])
    return show_point_cloud


show_point_cloud = show_point_cloud_node_group()

