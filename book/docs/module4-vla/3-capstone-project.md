# Chapter 3: Autonomous Humanoid Capstone Project

This capstone project brings together all the concepts from the previous modules to create an end-to-end autonomous humanoid robot simulation. You will integrate perception, navigation, manipulation, and LLM-based planning to enable a robot to complete a task based on a natural language command.

## Project Goal

The goal of this project is to create a simulation where a humanoid robot can fetch an object for a user based on a spoken command. For example, "bring me the soda from the kitchen."

## System Integration

This project requires integrating the following components:
-   **Isaac Sim**: To provide the simulated environment and robot.
-   **ROS 2**: As the communication backbone for all the components.
-   **Perception Pipeline**: An Isaac ROS pipeline for object detection and localization.
-   **Navigation Stack**: The Nav2 stack for moving the robot around the environment.
-   **Manipulation Controller**: A controller to execute picking and placing actions (e.g., using MoveIt).
-   **LLM Planner**: The Python script developed in the previous chapter to generate plans.
-   **Action Executor**: A new component that subscribes to the plan and makes the appropriate ROS 2 action or service calls.

## High-Level Workflow

1.  The user gives a command like "fetch the red block".
2.  The command is converted to text and sent to the LLM Planner.
3.  The LLM Planner, aware of the world state from the perception system, generates a plan: `[navigate_to(block_location), pick_up(red_block), navigate_to(user_location), place()]`.
4.  The Action Executor receives this plan and executes it step-by-step:
    a.  Sends a goal to the Nav2 stack.
    b.  Once the robot reaches the location, it calls the perception system to get the precise location of the red block.
    c.  It then calls the manipulation controller to pick up the block.
    d.  It continues with the rest of the plan until the task is complete.

In the next section, we will look at the launch file that brings all of these components together.

## Launching the Capstone Project

The following launch file is a simplified example of how you would start all the necessary nodes for the capstone project.

```python file=../../src/examples/vla/capstone.launch.py

```

To run this project, you would first need to ensure that Isaac Sim is running with your humanoid robot in the environment. Then, you can launch the capstone stack:

```bash
ros2 launch your_vla_package capstone.launch.py
```

After launching the stack, you can provide the robot with natural language commands and watch it execute the task!