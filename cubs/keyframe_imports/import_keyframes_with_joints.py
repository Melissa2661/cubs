import bpy
import math
from mathutils import Vector, Matrix, Quaternion
import json

def import_keyframes(joint_obj_path, data):
    """
    :param joint_obj_path: path to an object, eg three arrows showing canonical basis, to represent joints
    :param data: All the keyframe information, in json format. The information is imported from a 'Y up' environment.
    The expected format is as follows:
    {
    "bodies" :
    [
        {
            "id" (int),
            "init" (initial position of the center of mass, list):
            [
                x,
                y,
                z
            ],
            "mesh" (string, path to the .obj)
        },
        ... (one per body)
    ],
    "num_bodies" (int),
    "num_joints" (int),
    "transforms" : (list of transforms per body)
    [
        [ (one list per frame)
            { (for body 0)
                "orientation" (quaternion to represent rotation, as a list):
                [
                    w,
                    x,
                    y,
                    z
                ],
                "position" (position of the body):
                [
                    x,
                    y,
                    z
                ]
            },
            { (for body 1)
                ...
            },
        ],
        ...
    ],
    "transforms_j" : (list of transforms per hinge joint between body0 and body1, with relative position wrt joint r0 and r1, relative orientation wrt x-axis q0 and q1)
    [
        [ (one list per frame)
            { (for joint 0)
                "orientation" (global, equivalent to joint->q1):
                [
                    w,
                    x,
                    y,
                    z
                ],
                "orientation_p" (orientation of the parent, equivalent to joint->body1->q):
                [
                    w,
                    x,
                    y,
                    z
                ],
                "position" (global, calculated by joint->body0->x + joint->body0->q * joint->r0):
                [
                    x,
                    y,
                    z
                ]
            },
            { (for joint 1)
                ...
            },
        ],
        ...
    ]
    }
    """
    #
    # Just in case you want to reposition the keyframed objects without regenerating the keyframes
    # (Optional)
    #
    empty_parent = bpy.data.objects.new("Empty", None)
    bpy.context.collection.objects.link(empty_parent)
    #
    # Determine the number of frames
    #
    num_frames = len(data['transforms'])
    print("NUM_FRAMES : ", num_frames)
    frame_start = 1
    frame_end = num_frames
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = num_frames + 1
    #
    # Create rotation matrix to translate from "Y up" world to "Z up" world
    #
    y_to_z_offset = Quaternion(Vector((math.sqrt(0.5), math.sqrt(0.5), 0, 0)))
    num_bodies = data["num_bodies"]
    #
    # Importing the bodies
    #
    for i in range(0, num_bodies):
        fname = data["bodies"][i]["mesh"]
        print(fname)
        bpy.ops.wm.obj_import(filepath=fname)
        obj = bpy.context.active_object
        obj.parent = empty_parent
        obj.select_set(True)
        #
        # Init the simulation so that the object global position  fits the position of the convex hull
        #
        init_pos = data["bodies"][i]["init"]
        init = Vector((init_pos[0], init_pos[1], init_pos[2]))
        init.rotate(y_to_z_offset)
        bpy.context.scene.cursor.location = init
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")  # (type="ORIGIN_CENTER_OF_VOLUME")  # (type="ORIGIN_CURSOR")
        #
        for j in range(frame_start, frame_end):
            bpy.context.scene.frame_set(j)
            bpy.context.scene.frame_current = j
            # Translate the object
            pos = data['transforms'][j - 1][i]['position']
            loc = Vector((pos[0], pos[1], pos[2]))
            loc.rotate(y_to_z_offset)
            obj.location = loc
            # Save this translation as a keyframe
            obj.keyframe_insert(data_path='location')
            # Rotate the object
            ori = data['transforms'][j - 1][i]['orientation']
            q1 = Quaternion(ori)
            q1.rotate(y_to_z_offset)
            # Save this rotation as a keyframe
            obj.rotation_mode = 'QUATERNION'
            obj.rotation_quaternion = q1
            obj.keyframe_insert(data_path='rotation_quaternion')
        obj.select_set(False)
    #
    # Importing the joints
    #
    num_joints = data["num_joints"]
    bpy.context.scene.cursor.location = Vector((0, 0, 0))
    joint_list = []
    for i in range(0, num_joints):
        bpy.ops.wm.obj_import(filepath=joint_obj_path)
        obj = bpy.context.active_object
        obj.parent = empty_parent
        obj.select_set(True)
        joint_list.append(obj)
        #
        # Init the simulation so that the object global position  fits the position of the convex hull
        #
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")  # (type="ORIGIN_CENTER_OF_VOLUME")  # (type="ORIGIN_CURSOR")
        q_inv = y_to_z_offset.copy()
        q_inv.invert()
        #
        for j in range(frame_start, frame_end):
            bpy.context.scene.frame_set(j)
            bpy.context.scene.frame_current = j
            # Translate the object
            pos = data['transforms_j'][j - 1][i]['position']
            loc = Vector((pos[0], pos[1], pos[2]))
            loc.rotate(y_to_z_offset)
            obj.location = loc
            obj.keyframe_insert(data_path='location')
            # Rotate the object
            ori = data['transforms_j'][j - 1][i]['orientation']  # local orientation
            q1 = Quaternion(ori)
            q1.rotate(y_to_z_offset)
            ori_obj = data['transforms_j'][j - 1][i]['orientation_p']
            q2 = Quaternion(ori_obj)
            q2.rotate(y_to_z_offset)
            q1.rotate(q2)
            # Save rotation as keyframe
            obj.rotation_mode = 'QUATERNION'
            obj.rotation_quaternion = q1
            obj.keyframe_insert(data_path='rotation_quaternion')
        obj.select_set(False)
    for j in joint_list:
        j.select_set(True)
        bpy.context.view_layer.objects.active = j
    #
    # Links all the materials between the joints to not have thousands of copies of the same material
    #
    bpy.ops.object.make_links_data(type="MATERIAL")

keyframe_path = ""
obj_path = ""
with open(keyframe_path) as data_file:
    d = json.load(data_file)
    import_keyframes(obj_path, d)
