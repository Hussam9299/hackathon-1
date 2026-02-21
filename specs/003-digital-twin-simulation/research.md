# Research Outcomes: Module 2: The Digital Twin (Gazebo & Unity)

This document outlines the research tasks required to resolve the unknowns identified in the implementation plan. All research tasks are now complete.

## Research Tasks

### 1. Recommended Gazebo and Unity Versions

- **Task**: Determine the recommended versions of Gazebo and Unity that are most compatible with ROS 2 Humble and Foxy.
- **Goal**: Provide students with clear guidance on which versions of the simulators to install to ensure compatibility with the book's examples.
- **Outcome**: **Completed**.
    - **Gazebo**: The officially recommended Gazebo version for ROS 2 Humble is **Gazebo Fortress**. This version will be used for the book.
    - **Unity**: For Unity, **Unity 2021 LTS** is recommended. It is compatible with the official Unity Robotics package and provides a stable, long-term support release for students.

### 2. Best Practices for ROS 2 and Unity Integration

- **Task**: Investigate the best practices and available tools for integrating ROS 2 with Unity.
- **Goal**: Understand the common patterns and any official or community-supported plugins that facilitate communication between Unity and ROS 2.
- **Outcome**: **Completed**.
    - **Decision**: **Unity's official ROS-TCP-Connector** will be the recommended method for integrating ROS 2 with Unity.
    - **Rationale**: The official connector is well-documented, supported by Unity, and provides a straightforward setup process for students. It is suitable for the educational focus of this book.
    - **Alternatives considered**: Robotec.ai's "ROS2 For Unity" was considered but deemed too complex for the target audience. WebSocket-based solutions would require more manual setup.
