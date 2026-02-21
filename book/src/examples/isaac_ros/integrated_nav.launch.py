# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    """Launch the integrated navigation stack."""

    # Assuming vslam.launch.py is in the same directory
    vslam_launch_file = os.path.join(
        get_package_share_directory('your_package_name'),
        'launch',
        'vslam.launch.py'
    )

    # Nav2 launch
    nav2_launch_file = os.path.join(
        get_package_share_directory('nav2_bringup'),
        'launch',
        'bringup_launch.py'
    )

    return LaunchDescription([
        # Isaac Sim simulation - this would typically be launched separately
        # or through a dedicated Isaac Sim launch mechanism.
        # For simplicity, we assume it's running.

        # VSLAM
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(vslam_launch_file)
        ),

        # Nav2
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_file),
            launch_arguments={'use_sim_time': 'True'}.items(),
        ),
    ])
