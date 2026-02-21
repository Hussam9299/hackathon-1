from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    # Get the URDF file
    urdf_file_name = 'humanoid.urdf'
    urdf = os.path.join(
        get_package_share_directory('your_package_name'), # Replace with your package name
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}],
    )
    ld.add_action(robot_state_publisher_node)

    # Joint State Publisher GUI
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
    )
    ld.add_action(joint_state_publisher_gui_node)

    # RViz2
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(get_package_share_directory('your_package_name'), 'your_rviz_config.rviz')], # Replace with your rviz config
    )
    ld.add_action(rviz2_node)

    return ld
