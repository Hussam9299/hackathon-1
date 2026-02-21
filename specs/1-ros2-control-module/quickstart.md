# Quickstart Guide

This guide provides the steps to set up the development environment for the Docusaurus book and the ROS 2 code examples.

## Prerequisites

- **Node.js and npm**: Required for Docusaurus. Install from [nodejs.org](https://nodejs.org/).
- **ROS 2 Humble or Foxy**: The ROS 2 distribution used for the code examples. Follow the official installation guides:
    - [ROS 2 Humble (Ubuntu)](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
    - [ROS 2 Foxy (Ubuntu)](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
- **A code editor**: Such as Visual Studio Code.

## 1. Setting up the Docusaurus Book

The book's source code is in the `/book` directory of this repository.

1.  **Navigate to the book directory**:
    ```bash
    cd book
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Start the development server**:
    ```bash
    npm run start
    ```

    This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server. The site will be available at `http://localhost:3000`.

4.  **Build the static site**:
    ```bash
    npm run build
    ```

    This command generates static content into the `build` directory and can be served using any static contents hosting service. A clean build with no errors is a primary quality gate.

## 2. Running ROS 2 Examples

The Python code examples for ROS 2 are located within the project structure (the exact location will be determined by the "Content-Code Separation Strategy" research).

1.  **Source your ROS 2 environment**:
    Before running any ROS 2 command or script, you must source the setup file for your ROS 2 distribution.
    ```bash
    # For Humble
    source /opt/ros/humble/setup.bash

    # For Foxy
    source /opt/ros/foxy/setup.bash
    ```
    It is recommended to add this command to your `~/.bashrc` file.

2.  **Running a Python node**:
    To run a ROS 2 Python node, use the `ros2 run` command:
    ```bash
    # Example
    ros2 run <package_name> <executable_name>
    ```

    The chapters in the book will provide specific instructions for running each example.
