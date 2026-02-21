---
sidebar_position: 4
---

# Chapter 4: Bringing It All Together with Launch Files

In the previous chapters, we've created nodes, topics, services, and even a URDF model of our robot. We've been running each node in a separate terminal, which can be tedious.

In this chapter, we'll learn how to use **Launch Files** to start our entire robotic system with a single command.

## What are Launch Files?

A launch file is a Python script that allows you to start and configure multiple nodes at once. They are a powerful tool for managing complex robotic systems.

With launch files, you can:
- Start multiple nodes.
- Set parameters for your nodes.
- Remap topic names.
- And much more.

## Our Humanoid Launch File

Let's create a launch file for our humanoid robot. This launch file will start the `robot_state_publisher`, `joint_state_publisher_gui`, and `rviz2` nodes that we used in the previous chapter.

Create a file named `humanoid.launch.py` with the following content:

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    # Get the URDF file
    # Note: This is a simplified example. In a real project, you would use a package share directory.
    urdf_file_name = 'humanoid.urdf'
    urdf_path = os.path.abspath(urdf_file_name)


    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_path).read()}],
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
    )
    ld.add_action(rviz2_node)

    return ld
```

### Code Explained

- We import the necessary libraries from the `launch` and `launch_ros` packages.
- The `generate_launch_description` function is the entry point for the launch file.
- We create `Node` objects for each of the nodes we want to start.
- We add each `Node` object to the `LaunchDescription`.
- For the `robot_state_publisher`, we pass the URDF file content as a parameter.

Now, instead of opening three terminals, you can start everything with a single command.

## Running the Launch File

To run the launch file, open a terminal, navigate to the directory containing your `humanoid.launch.py` and `humanoid.urdf` files, and run the following command:

```bash
ros2 launch humanoid.launch.py
```

This single command will start the `robot_state_publisher`, `joint_state_publisher_gui`, and `rviz2`. You should see RViz2 open up, and you can use the joint state publisher GUI to move the robot's arms, just like before.

This concludes our introduction to the fundamental concepts of ROS 2. You've learned how to create nodes, communicate between them with topics and services, model a robot with URDF, and bring it all together with launch files. You are now ready to start building your own robotic applications with ROS 2.

