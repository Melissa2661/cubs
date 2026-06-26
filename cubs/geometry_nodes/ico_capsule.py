import bpy
import mathutils
import typing

# Based on https://blender.stackexchange.com/questions/346034/how-to-create-a-hexagonal-icosphere-style-capsule-in-geometry-nodes
# Adapted to use input arguments for length and radius


def capsule_of_ico_spheres_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Capsule of Ico Spheres node group"""
    capsule_of_ico_spheres_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Capsule of Ico Spheres")

    capsule_of_ico_spheres_1.color_tag = 'NONE'
    capsule_of_ico_spheres_1.description = ""
    capsule_of_ico_spheres_1.default_group_node_width = 140
    capsule_of_ico_spheres_1.is_modifier = True

    # capsule_of_ico_spheres_1 interface

    # Socket Geometry
    geometry_socket = capsule_of_ico_spheres_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'

    # Socket Geometry
    geometry_socket_1 = capsule_of_ico_spheres_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'

    # Socket Subdivisions
    subdivisions_socket = capsule_of_ico_spheres_1.interface.new_socket(name="Subdivisions", in_out='INPUT', socket_type='NodeSocketInt')
    subdivisions_socket.default_value = 2
    subdivisions_socket.min_value = 2
    subdivisions_socket.max_value = 6
    subdivisions_socket.subtype = 'NONE'
    subdivisions_socket.attribute_domain = 'POINT'
    subdivisions_socket.force_non_field = True

    # Socket Radius
    radius_socket = capsule_of_ico_spheres_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    radius_socket.default_value = 1.0
    radius_socket.min_value = 0.10000000149011612
    radius_socket.max_value = 10000.0
    radius_socket.subtype = 'NONE'
    radius_socket.attribute_domain = 'POINT'

    # Socket Approximate depth
    approximate_depth_socket = capsule_of_ico_spheres_1.interface.new_socket(name="Approximate depth", in_out='INPUT', socket_type='NodeSocketFloat')
    approximate_depth_socket.default_value = 3.0
    approximate_depth_socket.min_value = 0.10000000149011612
    approximate_depth_socket.max_value = 10000.0
    approximate_depth_socket.subtype = 'NONE'
    approximate_depth_socket.attribute_domain = 'POINT'
    approximate_depth_socket.force_non_field = True

    # Initialize capsule_of_ico_spheres_1 nodes

    # Node Position
    position = capsule_of_ico_spheres_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # Node Vector Rotate
    vector_rotate = capsule_of_ico_spheres_1.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.invert = False
    vector_rotate.rotation_type = 'AXIS_ANGLE'
    vector_rotate.inputs[1].hide = True
    vector_rotate.inputs[4].hide = True
    # Center
    vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Node Cylinder
    cylinder = capsule_of_ico_spheres_1.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.fill_type = 'NONE'
    # Side Segments
    cylinder.inputs[1].default_value = 1

    # Node Set Position
    set_position = capsule_of_ico_spheres_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Group Output
    group_output = capsule_of_ico_spheres_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Set Position.001
    set_position_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Selection
    set_position_001.inputs[1].default_value = True
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Triangulate
    triangulate = capsule_of_ico_spheres_1.nodes.new("GeometryNodeTriangulate")
    triangulate.name = "Triangulate"
    triangulate.ngon_method = 'BEAUTY'
    triangulate.quad_method = 'SHORTEST_DIAGONAL'
    # Selection
    triangulate.inputs[1].default_value = True

    # Node Group Input
    group_input = capsule_of_ico_spheres_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Math
    math = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Math.001
    math_001 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'DIVIDE'
    math_001.use_clamp = False
    # Value
    math_001.inputs[0].default_value = 3.1415927410125732

    # Node Math.002
    math_002 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'POWER'
    math_002.use_clamp = False
    # Value
    math_002.inputs[0].default_value = 2.0

    # Node Math.003
    math_003 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    # Value
    math_003.inputs[0].default_value = 10.0

    # Node Math.004
    math_004 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'DIVIDE'
    math_004.use_clamp = False

    # Node Math.005
    math_005 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'DIVIDE'
    math_005.use_clamp = False
    # Value_001
    math_005.inputs[1].default_value = 2.0

    # Node Math.006
    math_006 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'DIVIDE'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 2.0

    # Node Combine XYZ
    combine_xyz = capsule_of_ico_spheres_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # Node Ico Sphere
    ico_sphere = capsule_of_ico_spheres_1.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"

    # Node Group Input.001
    group_input_001 = capsule_of_ico_spheres_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"

    # Node Math.007
    math_007 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'ADD'
    math_007.use_clamp = False
    # Value_001
    math_007.inputs[1].default_value = 1.0

    # Node Position.001
    position_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    # Node Separate XYZ
    separate_xyz = capsule_of_ico_spheres_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    # Node Math.008
    math_008 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'LESS_THAN'
    math_008.use_clamp = False
    # Value_001
    math_008.inputs[1].default_value = 0.0

    # Node Delete Geometry
    delete_geometry = capsule_of_ico_spheres_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'

    # Node Set Position.002
    set_position_002 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    # Selection
    set_position_002.inputs[1].default_value = True
    # Position
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Group Input.002
    group_input_002 = capsule_of_ico_spheres_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"

    # Node Duplicate Elements.001
    duplicate_elements_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements_001.name = "Duplicate Elements.001"
    duplicate_elements_001.domain = 'INSTANCE'
    # Selection
    duplicate_elements_001.inputs[1].default_value = True

    # Node Rotate Instances
    rotate_instances = capsule_of_ico_spheres_1.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    # Selection
    rotate_instances.inputs[1].default_value = True
    # Local Space
    rotate_instances.inputs[4].default_value = True

    # Node Translate Instances
    translate_instances = capsule_of_ico_spheres_1.nodes.new("GeometryNodeTranslateInstances")
    translate_instances.name = "Translate Instances"
    # Selection
    translate_instances.inputs[1].default_value = True
    # Local Space
    translate_instances.inputs[3].default_value = True

    # Node Switch.001
    switch_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'ROTATION'
    # False
    switch_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # True
    switch_001.inputs[2].default_value = (0.0, 3.1415927410125732, 0.0)

    # Node Math.011
    math_011 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'MODULO'
    math_011.use_clamp = True
    # Value_001
    math_011.inputs[1].default_value = 2.0

    # Node Realize Instances
    realize_instances = capsule_of_ico_spheres_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 3

    # Node Geometry to Instance
    geometry_to_instance = capsule_of_ico_spheres_1.nodes.new("GeometryNodeGeometryToInstance")
    geometry_to_instance.name = "Geometry to Instance"

    # Node Math.012
    math_012 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = 'MULTIPLY'
    math_012.use_clamp = False

    # Node Combine XYZ.002
    combine_xyz_002 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    # X
    combine_xyz_002.inputs[0].default_value = 0.0
    # Y
    combine_xyz_002.inputs[1].default_value = 0.0

    # Node Merge by Distance
    merge_by_distance = capsule_of_ico_spheres_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    # Node Math.014
    math_014 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'DIVIDE'
    math_014.use_clamp = False

    # Node Math.015
    math_015 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'FLOOR'
    math_015.use_clamp = False

    # Node Math.016
    math_016 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'SUBTRACT'
    math_016.use_clamp = False

    # Node Join Geometry
    join_geometry = capsule_of_ico_spheres_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Set Position.004
    set_position_004 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeSetPosition")
    set_position_004.name = "Set Position.004"
    # Selection
    set_position_004.inputs[1].default_value = True
    # Position
    set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset
    set_position_004.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Math.013
    math_013 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'MULTIPLY'
    math_013.use_clamp = False

    # Node Combine XYZ.001
    combine_xyz_001 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    # X
    combine_xyz_001.inputs[0].default_value = 0.0
    # Y
    combine_xyz_001.inputs[1].default_value = 0.0

    # Node Switch
    switch = capsule_of_ico_spheres_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'ROTATION'
    # False
    switch.inputs[1].default_value = (0.0, 0.0, 0.0)

    # Node Transform Geometry
    transform_geometry = capsule_of_ico_spheres_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    # Translation
    transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Combine XYZ.003
    combine_xyz_003 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    # X
    combine_xyz_003.inputs[0].default_value = 0.0
    # Y
    combine_xyz_003.inputs[1].default_value = 0.0

    # Node Math.018
    math_018 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'MODULO'
    math_018.use_clamp = False
    # Value_001
    math_018.inputs[1].default_value = 2.0

    # Node Transform Geometry.001
    transform_geometry_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    # Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[2].default_value = (3.1415927410125732, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry.001
    join_geometry_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    # Node Merge by Distance.001
    merge_by_distance_001 = capsule_of_ico_spheres_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = 'ALL'
    # Selection
    merge_by_distance_001.inputs[1].default_value = True
    # Distance
    merge_by_distance_001.inputs[2].default_value = 0.0010000000474974513

    # Node Math.019
    math_019 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'DIVIDE'
    math_019.use_clamp = False
    # Value_001
    math_019.inputs[1].default_value = 2.0

    # Node Frame
    frame = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame.label = "Find depth that will result in equilateral triangle"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # Node Group Input.003
    group_input_003 = capsule_of_ico_spheres_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"

    # Node Frame.001
    frame_001 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_001.label = "Get vertices to coincide with ico sphere"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.002
    frame_002 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_002.label = "Spawn half of ico sphere"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_003.label = "Rotate to coincide with cylinder"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_004.label = "Number of segments to spawn"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_005.label = "Center of one segment"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Reroute
    reroute = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketFloat"
    # Node Vector
    vector = capsule_of_ico_spheres_1.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, 1.0)

    # Node Frame.006
    frame_006 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_006.label = "Make one cylinder segment"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # Node Frame.007
    frame_007 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_007.label = "Repeat cylinder segments"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    # Node Frame.008
    frame_008 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_008.label = "Depth"
    frame_008.name = "Frame.008"
    frame_008.use_custom_color = True
    frame_008.color = (0.2658196985721588, 0.2658196985721588, 0.2658196985721588)
    frame_008.label_size = 20
    frame_008.shrink = True

    # Node Frame.009
    frame_009 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_009.label = "Rotate even segments"
    frame_009.name = "Frame.009"
    frame_009.label_size = 20
    frame_009.shrink = True

    # Node Reroute.001
    reroute_001 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    # Node Frame.010
    frame_010 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_010.label = "Segment center"
    frame_010.name = "Frame.010"
    frame_010.use_custom_color = True
    frame_010.color = (0.16165919601917267, 0.1432710587978363, 0.6079999804496765)
    frame_010.label_size = 20
    frame_010.shrink = True

    # Node Frame.011
    frame_011 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_011.label = "Mirror all"
    frame_011.name = "Frame.011"
    frame_011.label_size = 20
    frame_011.shrink = True

    # Node Reroute.002
    reroute_002 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Reroute.003
    reroute_003 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketFloat"
    # Node Frame.012
    frame_012 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_012.label = "Segments to spawn"
    frame_012.name = "Frame.012"
    frame_012.use_custom_color = True
    frame_012.color = (0.3006298243999481, 0.3006298243999481, 0.3006298243999481)
    frame_012.label_size = 20
    frame_012.shrink = True

    # Node Reroute.005
    reroute_005 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketFloat"
    # Node Frame.013
    frame_013 = capsule_of_ico_spheres_1.nodes.new("NodeFrame")
    frame_013.label = "Depth"
    frame_013.name = "Frame.013"
    frame_013.use_custom_color = True
    frame_013.color = (0.2183513343334198, 0.2183513343334198, 0.2183513343334198)
    frame_013.label_size = 20
    frame_013.shrink = True

    # Node Reroute.004
    reroute_004 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketFloat"
    # Node Reroute.006
    reroute_006 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketFloat"
    # Node Reroute.007
    reroute_007 = capsule_of_ico_spheres_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloat"
    # Node Math.009
    math_009 = capsule_of_ico_spheres_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'MAXIMUM'
    math_009.use_clamp = False

    # Set parents
    capsule_of_ico_spheres_1.nodes["Position"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Vector Rotate"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Cylinder"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Set Position"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Set Position.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Triangulate"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Group Input"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Math"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Math.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.001"]
    capsule_of_ico_spheres_1.nodes["Math.002"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Math.003"].parent = capsule_of_ico_spheres_1.nodes["Frame.001"]
    capsule_of_ico_spheres_1.nodes["Math.004"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Math.005"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Math.006"].parent = capsule_of_ico_spheres_1.nodes["Frame.005"]
    capsule_of_ico_spheres_1.nodes["Combine XYZ"].parent = capsule_of_ico_spheres_1.nodes["Frame.005"]
    capsule_of_ico_spheres_1.nodes["Ico Sphere"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Group Input.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Math.007"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Position.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Separate XYZ"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Math.008"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Delete Geometry"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Set Position.002"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Group Input.002"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Rotate Instances"].parent = capsule_of_ico_spheres_1.nodes["Frame.009"]
    capsule_of_ico_spheres_1.nodes["Translate Instances"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Switch.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.009"]
    capsule_of_ico_spheres_1.nodes["Math.011"].parent = capsule_of_ico_spheres_1.nodes["Frame.009"]
    capsule_of_ico_spheres_1.nodes["Realize Instances"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Geometry to Instance"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Math.012"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Combine XYZ.002"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Merge by Distance"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Math.014"].parent = capsule_of_ico_spheres_1.nodes["Frame.004"]
    capsule_of_ico_spheres_1.nodes["Math.015"].parent = capsule_of_ico_spheres_1.nodes["Frame.004"]
    capsule_of_ico_spheres_1.nodes["Math.016"].parent = capsule_of_ico_spheres_1.nodes["Frame.004"]
    capsule_of_ico_spheres_1.nodes["Join Geometry"].parent = capsule_of_ico_spheres_1.nodes["Frame.011"]
    capsule_of_ico_spheres_1.nodes["Set Position.004"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Math.013"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Combine XYZ.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Switch"].parent = capsule_of_ico_spheres_1.nodes["Frame.003"]
    capsule_of_ico_spheres_1.nodes["Transform Geometry"].parent = capsule_of_ico_spheres_1.nodes["Frame.003"]
    capsule_of_ico_spheres_1.nodes["Combine XYZ.003"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Math.018"].parent = capsule_of_ico_spheres_1.nodes["Frame.003"]
    capsule_of_ico_spheres_1.nodes["Transform Geometry.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.011"]
    capsule_of_ico_spheres_1.nodes["Join Geometry.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.011"]
    capsule_of_ico_spheres_1.nodes["Merge by Distance.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.011"]
    capsule_of_ico_spheres_1.nodes["Math.019"].parent = capsule_of_ico_spheres_1.nodes["Frame.004"]
    capsule_of_ico_spheres_1.nodes["Group Input.003"].parent = capsule_of_ico_spheres_1.nodes["Frame.004"]
    capsule_of_ico_spheres_1.nodes["Frame.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Frame.003"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Frame.005"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Reroute"].parent = capsule_of_ico_spheres_1.nodes["Frame.008"]
    capsule_of_ico_spheres_1.nodes["Vector"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Frame.008"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Frame.009"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Reroute.001"].parent = capsule_of_ico_spheres_1.nodes["Frame.010"]
    capsule_of_ico_spheres_1.nodes["Frame.010"].parent = capsule_of_ico_spheres_1.nodes["Frame.007"]
    capsule_of_ico_spheres_1.nodes["Reroute.003"].parent = capsule_of_ico_spheres_1.nodes["Frame.012"]
    capsule_of_ico_spheres_1.nodes["Frame.012"].parent = capsule_of_ico_spheres_1.nodes["Frame.002"]
    capsule_of_ico_spheres_1.nodes["Reroute.005"].parent = capsule_of_ico_spheres_1.nodes["Frame.013"]
    capsule_of_ico_spheres_1.nodes["Frame.013"].parent = capsule_of_ico_spheres_1.nodes["Frame.006"]
    capsule_of_ico_spheres_1.nodes["Reroute.004"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Reroute.006"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Reroute.007"].parent = capsule_of_ico_spheres_1.nodes["Frame"]
    capsule_of_ico_spheres_1.nodes["Math.009"].parent = capsule_of_ico_spheres_1.nodes["Frame.004"]

    # Set locations
    capsule_of_ico_spheres_1.nodes["Position"].location = (572.6651000976562, -42.266357421875)
    capsule_of_ico_spheres_1.nodes["Vector Rotate"].location = (789.0946655273438, -124.688720703125)
    capsule_of_ico_spheres_1.nodes["Cylinder"].location = (741.6221313476562, -335.454833984375)
    capsule_of_ico_spheres_1.nodes["Set Position"].location = (1020.4611206054688, -227.9306640625)
    capsule_of_ico_spheres_1.nodes["Group Output"].location = (3167.70556640625, -16.973852157592773)
    capsule_of_ico_spheres_1.nodes["Set Position.001"].location = (1310.85009765625, -257.6259765625)
    capsule_of_ico_spheres_1.nodes["Triangulate"].location = (1490.73046875, -247.052734375)
    capsule_of_ico_spheres_1.nodes["Group Input"].location = (29.80029296875, -47.100341796875)
    capsule_of_ico_spheres_1.nodes["Math"].location = (219.3599853515625, -39.9287109375)
    capsule_of_ico_spheres_1.nodes["Math.001"].location = (243.70660400390625, -40.22528076171875)
    capsule_of_ico_spheres_1.nodes["Math.002"].location = (393.1173095703125, -46.965087890625)
    capsule_of_ico_spheres_1.nodes["Math.003"].location = (30.047607421875, -166.759521484375)
    capsule_of_ico_spheres_1.nodes["Math.004"].location = (587.2752685546875, -46.2894287109375)
    capsule_of_ico_spheres_1.nodes["Math.005"].location = (761.6346435546875, -41.3653564453125)
    capsule_of_ico_spheres_1.nodes["Math.006"].location = (30.02191162109375, -39.966796875)
    capsule_of_ico_spheres_1.nodes["Combine XYZ"].location = (231.9033203125, -73.39990234375)
    capsule_of_ico_spheres_1.nodes["Ico Sphere"].location = (390.82696533203125, -40.210235595703125)
    capsule_of_ico_spheres_1.nodes["Group Input.001"].location = (30.0498046875, -46.877471923828125)
    capsule_of_ico_spheres_1.nodes["Math.007"].location = (219.37762451171875, -164.62124633789062)
    capsule_of_ico_spheres_1.nodes["Position.001"].location = (401.355224609375, -192.576416015625)
    capsule_of_ico_spheres_1.nodes["Separate XYZ"].location = (568.1624755859375, -196.74273681640625)
    capsule_of_ico_spheres_1.nodes["Math.008"].location = (738.2273559570312, -166.69583129882812)
    capsule_of_ico_spheres_1.nodes["Delete Geometry"].location = (931.7482299804688, -42.501068115234375)
    capsule_of_ico_spheres_1.nodes["Set Position.002"].location = (1168.95751953125, -75.71151733398438)
    capsule_of_ico_spheres_1.nodes["Group Input.002"].location = (297.03192138671875, -450.265380859375)
    capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].location = (60.8297119140625, -340.0635986328125)
    capsule_of_ico_spheres_1.nodes["Rotate Instances"].location = (598.6650390625, -40.2030029296875)
    capsule_of_ico_spheres_1.nodes["Translate Instances"].location = (750.3253173828125, -185.36431884765625)
    capsule_of_ico_spheres_1.nodes["Switch.001"].location = (200.68994140625, -84.44677734375)
    capsule_of_ico_spheres_1.nodes["Math.011"].location = (29.974853515625, -164.1171875)
    capsule_of_ico_spheres_1.nodes["Realize Instances"].location = (1198.4742431640625, -315.9803466796875)
    capsule_of_ico_spheres_1.nodes["Geometry to Instance"].location = (50.96630859375, -236.62554931640625)
    capsule_of_ico_spheres_1.nodes["Math.012"].location = (390.1575927734375, -267.6283874511719)
    capsule_of_ico_spheres_1.nodes["Combine XYZ.002"].location = (568.2379150390625, -264.7743835449219)
    capsule_of_ico_spheres_1.nodes["Merge by Distance"].location = (1378.5035400390625, -215.69207763671875)
    capsule_of_ico_spheres_1.nodes["Math.014"].location = (642.4892578125, -110.62091064453125)
    capsule_of_ico_spheres_1.nodes["Math.015"].location = (996.405029296875, -108.66461181640625)
    capsule_of_ico_spheres_1.nodes["Math.016"].location = (463.761962890625, -104.59735107421875)
    capsule_of_ico_spheres_1.nodes["Join Geometry"].location = (29.94384765625, -111.29589080810547)
    capsule_of_ico_spheres_1.nodes["Set Position.004"].location = (567.7064208984375, -40.09197998046875)
    capsule_of_ico_spheres_1.nodes["Math.013"].location = (52.5487060546875, -612.8677978515625)
    capsule_of_ico_spheres_1.nodes["Combine XYZ.001"].location = (511.62127685546875, -388.1356201171875)
    capsule_of_ico_spheres_1.nodes["Switch"].location = (250.57867431640625, -97.63133239746094)
    capsule_of_ico_spheres_1.nodes["Transform Geometry"].location = (461.4974365234375, -40.11466979980469)
    capsule_of_ico_spheres_1.nodes["Combine XYZ.003"].location = (505.44866943359375, -662.1309814453125)
    capsule_of_ico_spheres_1.nodes["Math.018"].location = (29.8555908203125, -85.836669921875)
    capsule_of_ico_spheres_1.nodes["Transform Geometry.001"].location = (252.612548828125, -172.13653564453125)
    capsule_of_ico_spheres_1.nodes["Join Geometry.001"].location = (474.419921875, -89.67411041259766)
    capsule_of_ico_spheres_1.nodes["Merge by Distance.001"].location = (643.13671875, -39.92174530029297)
    capsule_of_ico_spheres_1.nodes["Math.019"].location = (816.0020751953125, -106.46820068359375)
    capsule_of_ico_spheres_1.nodes["Frame"].location = (-2120.0, -738.0)
    capsule_of_ico_spheres_1.nodes["Group Input.003"].location = (29.7734375, -103.52618408203125)
    capsule_of_ico_spheres_1.nodes["Frame.001"].location = (30.0, -40.0)
    capsule_of_ico_spheres_1.nodes["Frame.002"].location = (-962.5, 244.0)
    capsule_of_ico_spheres_1.nodes["Frame.003"].location = (988.0, -253.5)
    capsule_of_ico_spheres_1.nodes["Frame.004"].location = (-2350.0, -383.0)
    capsule_of_ico_spheres_1.nodes["Frame.005"].location = (607.5, -622.5)
    capsule_of_ico_spheres_1.nodes["Reroute"].location = (35.0, -45.0)
    capsule_of_ico_spheres_1.nodes["Vector"].location = (573.9400634765625, -111.90692138671875)
    capsule_of_ico_spheres_1.nodes["Frame.006"].location = (-1095.0, -894.0)
    capsule_of_ico_spheres_1.nodes["Frame.007"].location = (717.8961181640625, -199.5)
    capsule_of_ico_spheres_1.nodes["Frame.008"].location = (30.0, -564.360107421875)
    capsule_of_ico_spheres_1.nodes["Frame.009"].location = (369.1038818359375, -391.0)
    capsule_of_ico_spheres_1.nodes["Reroute.001"].location = (35.0, -45.0)
    capsule_of_ico_spheres_1.nodes["Frame.010"].location = (32.71746826171875, -676.24853515625)
    capsule_of_ico_spheres_1.nodes["Frame.011"].location = (2308.0, 80.0)
    capsule_of_ico_spheres_1.nodes["Reroute.002"].location = (-967.4974365234375, -670.402099609375)
    capsule_of_ico_spheres_1.nodes["Reroute.003"].location = (35.0, -45.0)
    capsule_of_ico_spheres_1.nodes["Frame.012"].location = (553.8294677734375, -539.8071899414062)
    capsule_of_ico_spheres_1.nodes["Reroute.005"].location = (35.0, -45.0)
    capsule_of_ico_spheres_1.nodes["Frame.013"].location = (163.74371337890625, -730.55126953125)
    capsule_of_ico_spheres_1.nodes["Reroute.004"].location = (223.5836181640625, -224.03759765625)
    capsule_of_ico_spheres_1.nodes["Reroute.006"].location = (533.853515625, -225.127197265625)
    capsule_of_ico_spheres_1.nodes["Reroute.007"].location = (592.112548828125, -225.023681640625)
    capsule_of_ico_spheres_1.nodes["Math.009"].location = (269.278076171875, -40.15106201171875)

    # Set dimensions
    capsule_of_ico_spheres_1.nodes["Position"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Position"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Vector Rotate"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Vector Rotate"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Cylinder"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Cylinder"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Set Position"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Set Position"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Group Output"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Group Output"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Set Position.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Set Position.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Triangulate"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Triangulate"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Group Input"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Group Input"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.002"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.002"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.003"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.003"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.004"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.004"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.005"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.005"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.006"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.006"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Combine XYZ"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Combine XYZ"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Ico Sphere"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Ico Sphere"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Group Input.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Group Input.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.007"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.007"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Position.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Position.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Separate XYZ"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Separate XYZ"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.008"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.008"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Delete Geometry"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Delete Geometry"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Set Position.002"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Set Position.002"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Group Input.002"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Group Input.002"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Rotate Instances"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Rotate Instances"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Translate Instances"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Translate Instances"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Switch.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Switch.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.011"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.011"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Realize Instances"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Realize Instances"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Geometry to Instance"].width  = 160.0
    capsule_of_ico_spheres_1.nodes["Geometry to Instance"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.012"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.012"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Combine XYZ.002"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Combine XYZ.002"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Merge by Distance"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Merge by Distance"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.014"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.014"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.015"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.015"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.016"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.016"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Join Geometry"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Join Geometry"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Set Position.004"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Set Position.004"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.013"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.013"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Combine XYZ.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Combine XYZ.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Switch"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Switch"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Transform Geometry"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Transform Geometry"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Combine XYZ.003"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Combine XYZ.003"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.018"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.018"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Transform Geometry.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Transform Geometry.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Join Geometry.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Join Geometry.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Merge by Distance.001"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Merge by Distance.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.019"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.019"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Frame"].width  = 931.5
    capsule_of_ico_spheres_1.nodes["Frame"].height = 260.127197265625

    capsule_of_ico_spheres_1.nodes["Group Input.003"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Group Input.003"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Frame.001"].width  = 413.5
    capsule_of_ico_spheres_1.nodes["Frame.001"].height = 346.0

    capsule_of_ico_spheres_1.nodes["Frame.002"].width  = 1649.5
    capsule_of_ico_spheres_1.nodes["Frame.002"].height = 811.0

    capsule_of_ico_spheres_1.nodes["Frame.003"].width  = 631.5
    capsule_of_ico_spheres_1.nodes["Frame.003"].height = 362.0

    capsule_of_ico_spheres_1.nodes["Frame.004"].width  = 1166.5
    capsule_of_ico_spheres_1.nodes["Frame.004"].height = 289.5

    capsule_of_ico_spheres_1.nodes["Frame.005"].width  = 402.0
    capsule_of_ico_spheres_1.nodes["Frame.005"].height = 222.5

    capsule_of_ico_spheres_1.nodes["Reroute"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Vector"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Vector"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Frame.006"].width  = 1660.5
    capsule_of_ico_spheres_1.nodes["Frame.006"].height = 875.0

    capsule_of_ico_spheres_1.nodes["Frame.007"].width  = 1548.6038818359375
    capsule_of_ico_spheres_1.nodes["Frame.007"].height = 803.5

    capsule_of_ico_spheres_1.nodes["Frame.008"].width  = 70.0
    capsule_of_ico_spheres_1.nodes["Frame.008"].height = 80.0

    capsule_of_ico_spheres_1.nodes["Frame.009"].width  = 768.5
    capsule_of_ico_spheres_1.nodes["Frame.009"].height = 382.5

    capsule_of_ico_spheres_1.nodes["Reroute.001"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.001"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Frame.010"].width  = 70.0
    capsule_of_ico_spheres_1.nodes["Frame.010"].height = 80.0

    capsule_of_ico_spheres_1.nodes["Frame.011"].width  = 813.0
    capsule_of_ico_spheres_1.nodes["Frame.011"].height = 556.0

    capsule_of_ico_spheres_1.nodes["Reroute.002"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.002"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Reroute.003"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.003"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Frame.012"].width  = 70.0
    capsule_of_ico_spheres_1.nodes["Frame.012"].height = 80.0

    capsule_of_ico_spheres_1.nodes["Reroute.005"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.005"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Frame.013"].width  = 70.0
    capsule_of_ico_spheres_1.nodes["Frame.013"].height = 80.0

    capsule_of_ico_spheres_1.nodes["Reroute.004"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.004"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Reroute.006"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.006"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Reroute.007"].width  = 20.0
    capsule_of_ico_spheres_1.nodes["Reroute.007"].height = 100.0

    capsule_of_ico_spheres_1.nodes["Math.009"].width  = 140.0
    capsule_of_ico_spheres_1.nodes["Math.009"].height = 100.0


    # Initialize capsule_of_ico_spheres_1 links

    # position.Position -> vector_rotate.Vector
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Position"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Vector Rotate"].inputs[0]
    )
    # vector_rotate.Vector -> set_position.Position
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Vector Rotate"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position"].inputs[2]
    )
    # cylinder.Mesh -> set_position.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Cylinder"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position"].inputs[0]
    )
    # set_position.Geometry -> set_position_001.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Set Position"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position.001"].inputs[0]
    )
    # set_position_001.Geometry -> triangulate.Mesh
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Set Position.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Triangulate"].inputs[0]
    )
    # group_input.Subdivisions -> math.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input"].outputs[1],
        capsule_of_ico_spheres_1.nodes["Math"].inputs[0]
    )
    # math_001.Value -> vector_rotate.Angle
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Vector Rotate"].inputs[3]
    )
    # math.Value -> math_002.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.002"].inputs[1]
    )
    # math_006.Value -> combine_xyz.Z
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.006"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Combine XYZ"].inputs[2]
    )
    # cylinder.Top -> set_position.Selection
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Cylinder"].outputs[1],
        capsule_of_ico_spheres_1.nodes["Set Position"].inputs[1]
    )
    # math_003.Value -> math_001.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.003"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.001"].inputs[1]
    )
    # group_input_001.Subdivisions -> math_007.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input.001"].outputs[1],
        capsule_of_ico_spheres_1.nodes["Math.007"].inputs[0]
    )
    # math_007.Value -> ico_sphere.Subdivisions
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.007"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Ico Sphere"].inputs[1]
    )
    # position_001.Position -> separate_xyz.Vector
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Position.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Separate XYZ"].inputs[0]
    )
    # separate_xyz.Z -> math_008.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Separate XYZ"].outputs[2],
        capsule_of_ico_spheres_1.nodes["Math.008"].inputs[0]
    )
    # math_008.Value -> delete_geometry.Selection
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.008"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Delete Geometry"].inputs[1]
    )
    # ico_sphere.Mesh -> delete_geometry.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Ico Sphere"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Delete Geometry"].inputs[0]
    )
    # delete_geometry.Geometry -> set_position_002.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Delete Geometry"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position.002"].inputs[0]
    )
    # math_003.Value -> cylinder.Vertices
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.003"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Cylinder"].inputs[0]
    )
    # group_input_002.Radius -> cylinder.Radius
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input.002"].outputs[2],
        capsule_of_ico_spheres_1.nodes["Cylinder"].inputs[3]
    )
    # math_011.Value -> switch_001.Switch
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.011"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Switch.001"].inputs[0]
    )
    # duplicate_elements_001.Duplicate Index -> math_011.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].outputs[1],
        capsule_of_ico_spheres_1.nodes["Math.011"].inputs[0]
    )
    # geometry_to_instance.Instances -> duplicate_elements_001.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Geometry to Instance"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].inputs[0]
    )
    # triangulate.Mesh -> geometry_to_instance.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Triangulate"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Geometry to Instance"].inputs[0]
    )
    # math_012.Value -> combine_xyz_002.Z
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.012"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Combine XYZ.002"].inputs[2]
    )
    # duplicate_elements_001.Duplicate Index -> math_012.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].outputs[1],
        capsule_of_ico_spheres_1.nodes["Math.012"].inputs[0]
    )
    # combine_xyz_002.Vector -> translate_instances.Translation
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Combine XYZ.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Translate Instances"].inputs[2]
    )
    # switch_001.Output -> rotate_instances.Rotation
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Switch.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Rotate Instances"].inputs[2]
    )
    # translate_instances.Instances -> rotate_instances.Instances
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Translate Instances"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Rotate Instances"].inputs[0]
    )
    # set_position_004.Geometry -> translate_instances.Instances
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Set Position.004"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Translate Instances"].inputs[0]
    )
    # realize_instances.Geometry -> merge_by_distance.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Realize Instances"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Merge by Distance"].inputs[0]
    )
    # math_004.Value -> math_005.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.004"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.005"].inputs[0]
    )
    # math_019.Value -> math_015.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.019"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.015"].inputs[0]
    )
    # merge_by_distance.Geometry -> join_geometry.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Merge by Distance"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Join Geometry"].inputs[0]
    )
    # merge_by_distance_001.Geometry -> group_output.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Merge by Distance.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Group Output"].inputs[0]
    )
    # group_input_001.Radius -> ico_sphere.Radius
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input.001"].outputs[2],
        capsule_of_ico_spheres_1.nodes["Ico Sphere"].inputs[0]
    )
    # combine_xyz.Vector -> set_position_001.Offset
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Combine XYZ"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position.001"].inputs[3]
    )
    # duplicate_elements_001.Geometry -> set_position_004.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position.004"].inputs[0]
    )
    # math_016.Value -> math_014.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.016"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.014"].inputs[0]
    )
    # math_005.Value -> math_014.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.005"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.014"].inputs[1]
    )
    # math_005.Value -> math_013.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.005"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.013"].inputs[0]
    )
    # math_013.Value -> combine_xyz_001.Z
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.013"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Combine XYZ.001"].inputs[2]
    )
    # combine_xyz_001.Vector -> set_position_002.Offset
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Combine XYZ.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Set Position.002"].inputs[3]
    )
    # set_position_002.Geometry -> transform_geometry.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Set Position.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Transform Geometry"].inputs[0]
    )
    # switch.Output -> transform_geometry.Rotation
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Switch"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Transform Geometry"].inputs[2]
    )
    # math_001.Value -> combine_xyz_003.Z
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Combine XYZ.003"].inputs[2]
    )
    # combine_xyz_003.Vector -> switch.True
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Combine XYZ.003"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Switch"].inputs[2]
    )
    # math_018.Value -> switch.Switch
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.018"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Switch"].inputs[0]
    )
    # join_geometry.Geometry -> transform_geometry_001.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Join Geometry"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # transform_geometry_001.Geometry -> join_geometry_001.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Transform Geometry.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Join Geometry.001"].inputs[0]
    )
    # join_geometry_001.Geometry -> merge_by_distance_001.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Join Geometry.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Merge by Distance.001"].inputs[0]
    )
    # math_014.Value -> math_019.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.014"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.019"].inputs[0]
    )
    # group_input_003.Radius -> math_016.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input.003"].outputs[2],
        capsule_of_ico_spheres_1.nodes["Math.016"].inputs[1]
    )
    # reroute.Output -> math_012.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.012"].inputs[1]
    )
    # vector.Vector -> vector_rotate.Axis
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Vector"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Vector Rotate"].inputs[2]
    )
    # rotate_instances.Instances -> realize_instances.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Rotate Instances"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Realize Instances"].inputs[0]
    )
    # combine_xyz.Vector -> reroute_001.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Combine XYZ"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> rotate_instances.Pivot Point
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.001"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Rotate Instances"].inputs[3]
    )
    # math_015.Value -> reroute_002.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.015"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute.002"].inputs[0]
    )
    # reroute_002.Output -> reroute_003.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_003.Output -> math_018.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.003"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.018"].inputs[0]
    )
    # reroute_002.Output -> math_013.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.013"].inputs[1]
    )
    # math_005.Value -> reroute.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.005"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute"].inputs[0]
    )
    # math_005.Value -> reroute_005.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.005"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_005.Output -> math_006.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.005"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.006"].inputs[0]
    )
    # reroute_005.Output -> cylinder.Depth
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.005"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Cylinder"].inputs[4]
    )
    # group_input.Radius -> reroute_004.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input"].outputs[2],
        capsule_of_ico_spheres_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_004.Output -> reroute_006.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.004"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute.006"].inputs[0]
    )
    # reroute_006.Output -> math_004.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.006"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.004"].inputs[0]
    )
    # math_002.Value -> math_004.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.004"].inputs[1]
    )
    # reroute_007.Output -> math_003.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.007"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.003"].inputs[1]
    )
    # math_002.Value -> reroute_007.Input
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_002.Output -> duplicate_elements_001.Amount
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Reroute.002"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Duplicate Elements.001"].inputs[2]
    )
    # group_input_003.Radius -> math_009.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input.003"].outputs[2],
        capsule_of_ico_spheres_1.nodes["Math.009"].inputs[0]
    )
    # group_input_003.Approximate depth -> math_009.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Group Input.003"].outputs[3],
        capsule_of_ico_spheres_1.nodes["Math.009"].inputs[1]
    )
    # math_009.Value -> math_016.Value
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Math.009"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Math.016"].inputs[0]
    )
    # transform_geometry.Geometry -> join_geometry.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Transform Geometry"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Join Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> join_geometry_001.Geometry
    capsule_of_ico_spheres_1.links.new(
        capsule_of_ico_spheres_1.nodes["Join Geometry"].outputs[0],
        capsule_of_ico_spheres_1.nodes["Join Geometry.001"].inputs[0]
    )

    return capsule_of_ico_spheres_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    capsule_of_ico_spheres = capsule_of_ico_spheres_1_node_group(node_tree_names)
    node_tree_names[capsule_of_ico_spheres_1_node_group] = capsule_of_ico_spheres.name

