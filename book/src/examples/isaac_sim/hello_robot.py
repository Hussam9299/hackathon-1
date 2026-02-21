# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
from omni.isaac.kit import SimulationApp

# This is a simplified example.
# For a full example, please refer to the Isaac Sim documentation.

simulation_app = SimulationApp({"headless": False})

from omni.isaac.core import World
from omni.isaac.core.objects import VisualCuboid

# Create a new world
world = World()

# Add a cube to the world
world.scene.add(
    VisualCuboid(
        prim_path="/new_cube",
        name="my_cube",
        position=[0, 0, 1.0],
        scale=[0.5, 0.5, 0.5],
        color=[1.0, 0, 0],
    )
)

# Reset the world to the initial state
world.reset()

# Simulate for a few steps
for i in range(100):
    world.step(render=True)

simulation_app.close()
