# Data Model: Module 2: The Digital Twin (Gazebo & Unity)

This document defines the key entities for the "Digital Twin" module.

## 1. Digital Twin

A `Digital Twin` is a virtual representation of a physical robot. It encompasses the robot's visual appearance, its kinematic structure, and its simulated sensors.

- **Key Attributes**:
    - `Robot Model`: The 3D model of the robot (e.g., in URDF or FBX format).
    - `Sensors`: A collection of simulated sensors attached to the robot.
- **Relationships**:
    - A Digital Twin exists within a `Gazebo World` or a `Unity Scene`.

## 2. Gazebo World

A `Gazebo World` is a simulation environment within the Gazebo simulator. It contains robot models, objects, and defines the physics properties of the environment.

- **Key Attributes**:
    - `Environment`: The static environment, including ground planes, walls, and other objects.
    - `Physics Properties`: Gravity, friction, and other physical parameters.
    - `Robot Models`: One or more robot models loaded into the world.

## 3. Unity Scene

A `Unity Scene` is a simulation environment within the Unity game engine. It is used for creating high-fidelity digital twins with realistic visuals.

- **Key Attributes**:
    - `Environment`: The 3D environment, including lighting, materials, and textures.
    - `Robot Models`: One or more robot models imported into the scene.
    - `Scripts`: C# scripts that can be used to control the behavior of objects in the scene.

## 4. Simulated Sensor

A `Simulated Sensor` is a virtual sensor that generates data as if it were on a real robot.

- **Types**:
    - `LiDAR`: Generates a 2D or 3D point cloud of the environment.
    - `Depth Camera`: Generates an image where each pixel represents the distance to an object.
    - `IMU (Inertial Measurement Unit)`: Measures the robot's orientation and acceleration.
- **Key Attributes**:
    - `Update Rate`: The frequency at which the sensor generates data.
    - `Noise Model`: A model of the sensor's noise characteristics.
- **Relationships**:
    - A Simulated Sensor is attached to a `link` of a `Robot Model`.
