# A simplified example of a launch file for the capstone project.
# This file would be much more complex in a real-world scenario.

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    """Launch the capstone project."""

    # Assuming other launch files are available in the project
    isaac_ros_launch_path = get_package_share_directory('your_isaac_ros_package')
    nav2_launch_path = get_package_share_directory('nav2_bringup')
    vla_pkg_path = get_package_share_directory('your_vla_package')


    return LaunchDescription([
        # Perception
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(isaac_ros_launch_path, 'launch', 'isaac_ros_vslam.launch.py')
            )
        ),

        # Navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_path, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={'use_sim_time': 'True'}.items(),
        ),

        # LLM Planner Node
        Node(
            package='your_vla_package',
            executable='llm_planner_node.py',
            name='llm_planner'
        ),

        # Action Executor Node
        Node(
            package='your_vla_package',
            executable='action_executor_node.py',
            name='action_executor'
        ),
    ])
