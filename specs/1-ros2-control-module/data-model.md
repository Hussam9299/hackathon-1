# Data Model

This document defines the key entities for the "Robotic Nervous System (ROS 2)" module, as identified in the feature specification.

## 1. ROS 2 Node

A `Node` is the fundamental process unit in a ROS 2 system. It is an executable that performs a specific task, such as controlling a motor, reading a sensor, or planning a path.

- **Key Attributes**:
    - `name` (string): A unique identifier for the node within the ROS 2 graph.
    - `namespace` (string, optional): A prefix that groups related nodes, preventing name collisions.
- **Relationships**:
    - A Node can have multiple Publishers, Subscribers, Services, and Clients.
- **State**:
    - A node can be in various lifecycle states (e.g., `unconfigured`, `inactive`, `active`, `finalized`) if it is a "Lifecycle Node". For this module, we will primarily use standard nodes without lifecycle management.

## 2. ROS 2 Topic

A `Topic` is a named bus over which nodes exchange messages. Topics use a publisher-subscriber pattern for anonymous, one-to-many communication.

- **Key Attributes**:
    - `name` (string): The unique name of the topic (e.g., `/cmd_vel`).
    - `message_type` (string): The data structure of the messages published on the topic (e.g., `std_msgs/String`, `geometry_msgs/Twist`).
- **Relationships**:
    - A Topic can have one or more Publishers and one or more Subscribers.
    - Publishers and Subscribers must use the same `message_type` to communicate.

## 3. URDF Model (Unified Robot Description Format)

A `URDF` is an XML file that represents a robot model, specifying its physical structure and kinematic properties.

- **Key Components**:
    - `<robot name="...">`: The root element of the model.
    - `<link name="...">`: Describes a rigid body part of the robot. It has properties for inertia, visual appearance (`<visual>`), and collision geometry (`<collision>`).
    - `<joint name="..." type="...">`: Describes the kinematic relationship between two links.
        - `type`: Can be `revolute`, `continuous`, `prismatic`, `fixed`, `floating`, or `planar`.
        - `parent` (link): The parent link of the joint.
        - `child` (link): The child link of the joint.
        - `origin`: Specifies the transform from the parent link to the child link.
- **Validation Rules**:
    - The URDF must be a well-formed XML.
    - The model must form a tree structure (no loops).
    - Every joint must have a parent and a child link.
    - The `check_urdf` command-line tool is used to validate the URDF file against these rules.
