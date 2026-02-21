# Quickstart Guide: Module 2: The Digital Twin (Gazebo & Unity)

This guide provides the steps to set up the development environment for Gazebo and Unity.

## Prerequisites

- **ROS 2 Humble or Foxy**: The ROS 2 distribution used for the code examples.
- **A code editor**: Such as Visual Studio Code.

## 1. Setting up Gazebo

1.  **Install Gazebo Fortress**: Follow the official installation instructions for Gazebo Fortress.
    ```bash
    sudo apt-get install gz-fortress
    ```

2.  **Install ROS 2 Gazebo packages**:
    ```bash
    sudo apt-get install ros-humble-ros-gz
    ```

3.  **Running a Gazebo simulation**:
    You can run a Gazebo world with the following command:
    ```bash
    gz sim shapes.sdf
    ```

## 2. Setting up Unity

1.  **Install Unity Hub**: Download and install Unity Hub from the official Unity website.

2.  **Install Unity 2021 LTS**: Use Unity Hub to install Unity 2021 LTS.

3.  **Install the Unity Robotics package**:
    - Open a new Unity project.
    - Go to `Window > Package Manager`.
    - Click the `+` icon and select `Add package from git URL...`.
    - Enter `com.unity.robotics.ros-tcp-connector` and click `Add`.

4.  **Running a Unity simulation**:
    - Open your Unity scene.
    - Click the "Play" button at the top of the editor.
