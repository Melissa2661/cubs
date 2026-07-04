import bpy
import mathutils
import os
import typing

# This is Blender's Smooth by Angle node.
# When using the python editor from the GUI, this is easier accessed as:
#   bpy.ops.object.modifier_add_node_group(asset_library_type='ESSENTIALS', asset_library_identifier="", relative_asset_identifier=r"geometry_nodes\smooth_by_angle.blend\NodeTree\Smooth by Angle")
# However, when running blender as a background app, this operation causes sync issues.
# See https://projects.blender.org/blender/blender/issues/117399 for more information.


def _smooth_by_angle_1_node_group():
    """Initialize Smooth by Angle node group"""
    smooth_by_angle_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Smooth by Angle")

    smooth_by_angle_1.color_tag = 'GEOMETRY'
    smooth_by_angle_1.description = "Set the sharpness of mesh edges based on the angle between the neighboring faces"
    smooth_by_angle_1.default_group_node_width = 140
    smooth_by_angle_1.is_modifier = True

    # smooth_by_angle_1 interface

    # Socket Mesh
    mesh_socket = smooth_by_angle_1.interface.new_socket(name="Mesh", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    mesh_socket.attribute_domain = 'POINT'

    # Socket Mesh
    mesh_socket_1 = smooth_by_angle_1.interface.new_socket(name="Mesh", in_out='INPUT', socket_type='NodeSocketGeometry')
    mesh_socket_1.attribute_domain = 'POINT'

    # Socket Angle
    angle_socket = smooth_by_angle_1.interface.new_socket(name="Angle", in_out='INPUT', socket_type='NodeSocketFloat')
    angle_socket.default_value = 0.5235987901687622
    angle_socket.min_value = 0.0
    angle_socket.max_value = 3.1415927410125732
    angle_socket.subtype = 'ANGLE'
    angle_socket.attribute_domain = 'POINT'
    angle_socket.description = "Maximum face angle for smooth edges"

    # Socket Ignore Sharpness
    ignore_sharpness_socket = smooth_by_angle_1.interface.new_socket(name="Ignore Sharpness", in_out='INPUT', socket_type='NodeSocketBool')
    ignore_sharpness_socket.default_value = False
    ignore_sharpness_socket.attribute_domain = 'POINT'
    ignore_sharpness_socket.force_non_field = True

    # Initialize smooth_by_angle_1 nodes

    # Node Set Shade Smooth
    set_shade_smooth = smooth_by_angle_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'EDGE'

    # Node Set Shade Smooth.001
    set_shade_smooth_001 = smooth_by_angle_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_001.name = "Set Shade Smooth.001"
    set_shade_smooth_001.domain = 'FACE'
    # Selection
    set_shade_smooth_001.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_001.inputs[2].default_value = True

    # Node Group Output
    group_output = smooth_by_angle_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Edge Angle
    edge_angle = smooth_by_angle_1.nodes.new("GeometryNodeInputMeshEdgeAngle")
    edge_angle.name = "Edge Angle"

    # Node Group Input
    group_input = smooth_by_angle_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True

    # Node Is Edge Smooth
    is_edge_smooth = smooth_by_angle_1.nodes.new("GeometryNodeInputEdgeSmooth")
    is_edge_smooth.name = "Is Edge Smooth"

    # Node Is Shade Smooth
    is_shade_smooth = smooth_by_angle_1.nodes.new("GeometryNodeInputShadeSmooth")
    is_shade_smooth.name = "Is Shade Smooth"

    # Node Compare
    compare = smooth_by_angle_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_EQUAL'

    # Node Boolean Math.001
    boolean_math_001 = smooth_by_angle_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'AND'

    # Node Group Input.001
    group_input_001 = smooth_by_angle_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True

    # Node Group Input.002
    group_input_002 = smooth_by_angle_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True

    # Node Boolean Math
    boolean_math = smooth_by_angle_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'OR'

    # Node Boolean Math.002
    boolean_math_002 = smooth_by_angle_1.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = 'OR'

    # Node Group Input.003
    group_input_003 = smooth_by_angle_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[3].hide = True

    # Set locations
    smooth_by_angle_1.nodes["Set Shade Smooth"].location = (120.0, -80.0)
    smooth_by_angle_1.nodes["Set Shade Smooth.001"].location = (300.0, -80.0)
    smooth_by_angle_1.nodes["Group Output"].location = (480.0, -80.0)
    smooth_by_angle_1.nodes["Edge Angle"].location = (-440.0, -240.0)
    smooth_by_angle_1.nodes["Group Input"].location = (-80.0, -80.0)
    smooth_by_angle_1.nodes["Is Edge Smooth"].location = (-260.0, -120.0)
    smooth_by_angle_1.nodes["Is Shade Smooth"].location = (-439.5191650390625, -396.6327819824219)
    smooth_by_angle_1.nodes["Compare"].location = (-260.0, -260.0)
    smooth_by_angle_1.nodes["Boolean Math.001"].location = (-80.0, -260.0)
    smooth_by_angle_1.nodes["Group Input.001"].location = (-439.5191650390625, -329.1396179199219)
    smooth_by_angle_1.nodes["Group Input.002"].location = (-259.0383605957031, -188.6585693359375)
    smooth_by_angle_1.nodes["Boolean Math"].location = (-80.0, -149.1396026611328)
    smooth_by_angle_1.nodes["Boolean Math.002"].location = (-260.0, -380.0)
    smooth_by_angle_1.nodes["Group Input.003"].location = (-440.0, -460.0)

    # Set dimensions
    smooth_by_angle_1.nodes["Set Shade Smooth"].width  = 140.0
    smooth_by_angle_1.nodes["Set Shade Smooth"].height = 100.0

    smooth_by_angle_1.nodes["Set Shade Smooth.001"].width  = 140.0
    smooth_by_angle_1.nodes["Set Shade Smooth.001"].height = 100.0

    smooth_by_angle_1.nodes["Group Output"].width  = 140.0
    smooth_by_angle_1.nodes["Group Output"].height = 100.0

    smooth_by_angle_1.nodes["Edge Angle"].width  = 140.0
    smooth_by_angle_1.nodes["Edge Angle"].height = 100.0

    smooth_by_angle_1.nodes["Group Input"].width  = 140.0
    smooth_by_angle_1.nodes["Group Input"].height = 100.0

    smooth_by_angle_1.nodes["Is Edge Smooth"].width  = 140.0
    smooth_by_angle_1.nodes["Is Edge Smooth"].height = 100.0

    smooth_by_angle_1.nodes["Is Shade Smooth"].width  = 140.0
    smooth_by_angle_1.nodes["Is Shade Smooth"].height = 100.0

    smooth_by_angle_1.nodes["Compare"].width  = 140.0
    smooth_by_angle_1.nodes["Compare"].height = 100.0

    smooth_by_angle_1.nodes["Boolean Math.001"].width  = 140.0
    smooth_by_angle_1.nodes["Boolean Math.001"].height = 100.0

    smooth_by_angle_1.nodes["Group Input.001"].width  = 140.0
    smooth_by_angle_1.nodes["Group Input.001"].height = 100.0

    smooth_by_angle_1.nodes["Group Input.002"].width  = 140.0
    smooth_by_angle_1.nodes["Group Input.002"].height = 100.0

    smooth_by_angle_1.nodes["Boolean Math"].width  = 140.0
    smooth_by_angle_1.nodes["Boolean Math"].height = 100.0

    smooth_by_angle_1.nodes["Boolean Math.002"].width  = 140.0
    smooth_by_angle_1.nodes["Boolean Math.002"].height = 100.0

    smooth_by_angle_1.nodes["Group Input.003"].width  = 140.0
    smooth_by_angle_1.nodes["Group Input.003"].height = 100.0


    # Initialize smooth_by_angle_1 links

    # edge_angle.Unsigned Angle -> compare.A
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Edge Angle"].outputs[0],
        smooth_by_angle_1.nodes["Compare"].inputs[0]
    )
    # set_shade_smooth_001.Geometry -> group_output.Mesh
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Set Shade Smooth.001"].outputs[0],
        smooth_by_angle_1.nodes["Group Output"].inputs[0]
    )
    # group_input_001.Angle -> compare.B
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Group Input.001"].outputs[1],
        smooth_by_angle_1.nodes["Compare"].inputs[1]
    )
    # compare.Result -> boolean_math_001.Boolean
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Compare"].outputs[0],
        smooth_by_angle_1.nodes["Boolean Math.001"].inputs[0]
    )
    # group_input.Mesh -> set_shade_smooth.Geometry
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Group Input"].outputs[0],
        smooth_by_angle_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # set_shade_smooth.Geometry -> set_shade_smooth_001.Geometry
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Set Shade Smooth"].outputs[0],
        smooth_by_angle_1.nodes["Set Shade Smooth.001"].inputs[0]
    )
    # boolean_math_001.Boolean -> set_shade_smooth.Shade Smooth
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Boolean Math.001"].outputs[0],
        smooth_by_angle_1.nodes["Set Shade Smooth"].inputs[2]
    )
    # group_input_002.Ignore Sharpness -> boolean_math.Boolean
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Group Input.002"].outputs[2],
        smooth_by_angle_1.nodes["Boolean Math"].inputs[1]
    )
    # is_edge_smooth.Smooth -> boolean_math.Boolean
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Is Edge Smooth"].outputs[0],
        smooth_by_angle_1.nodes["Boolean Math"].inputs[0]
    )
    # boolean_math.Boolean -> set_shade_smooth.Selection
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Boolean Math"].outputs[0],
        smooth_by_angle_1.nodes["Set Shade Smooth"].inputs[1]
    )
    # group_input_003.Ignore Sharpness -> boolean_math_002.Boolean
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Group Input.003"].outputs[2],
        smooth_by_angle_1.nodes["Boolean Math.002"].inputs[1]
    )
    # is_shade_smooth.Smooth -> boolean_math_002.Boolean
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Is Shade Smooth"].outputs[0],
        smooth_by_angle_1.nodes["Boolean Math.002"].inputs[0]
    )
    # boolean_math_002.Boolean -> boolean_math_001.Boolean
    smooth_by_angle_1.links.new(
        smooth_by_angle_1.nodes["Boolean Math.002"].outputs[0],
        smooth_by_angle_1.nodes["Boolean Math.001"].inputs[1]
    )

    return smooth_by_angle_1


def get_smooth_by_angle():
    """
    | Smooth by angle node, as auto-generated by Blender.
    | Controls: Angle, Ignore Sharpness
    """
    smooth_by_angle = _smooth_by_angle_1_node_group()
    return smooth_by_angle
