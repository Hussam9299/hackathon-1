# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """Launch the Isaac ROS VSLAM pipeline."""
    return LaunchDescription([
        Node(
            package='isaac_ros_visual_slam',
            executable='visual_slam_node',
            name='isaac_visual_slam',
            parameters=[{
                'use_sim_time': True,
                # Add other parameters here
            }],
            remappings=[
                # Add remappings here
            ]
        )
    ])
