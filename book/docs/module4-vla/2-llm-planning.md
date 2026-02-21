# Chapter 2: LLM-based Planning

A key component of our VLA pipeline is the LLM Planner. This chapter explains how to use a Large Language Model (LLM) to transform a high-level natural language command into a sequence of concrete steps that a robot can execute.

## The Role of the LLM

The LLM acts as the "brain" of the robot's decision-making process. Its task is to:
1.  **Understand the User's Intent**: Parse the natural language command to understand what the user wants to achieve.
2.  **Reason about the World**: Take into account the current state of the environment (e.g., from the perception system) to form a feasible plan.
3.  **Generate a Plan**: Decompose the high-level goal into a sequence of simpler, actionable steps.

## Prompt Engineering for Robotic Planning

To get the LLM to generate a useful plan, we need to provide it with a carefully crafted prompt. This is known as "prompt engineering". A good prompt for robotic planning should include:
-   **The Goal**: The user's command.
-   **The Context**: A description of the current environment, including the robot's state and the objects it can perceive.
-   **The available actions**: A list of the high-level actions the robot can perform (e.g., `navigate_to(location)`, `pick_up(object)`, `place(location)`).
-   **The desired output format**: Instructions on how the LLM should format its response, for example, as a JSON array of actions.

## Example: From Prompt to Plan

Let's say the user command is "bring me the apple from the table".

The prompt we send to the LLM might look something like this:

```
You are a helpful robot assistant. Your task is to create a plan to achieve a goal.
The user's goal is: "bring me the apple from the table".

Current world state:
- Robot is at the charging station.
- An apple is on the kitchen table.
- The user is in the living room.

Available actions:
- navigate_to(location)
- pick_up(object)
- place_at(location)

Output the plan as a JSON array of actions.
```

The LLM would then process this prompt and might return the following plan:

```json
[
  { "action": "navigate_to", "parameters": ["kitchen table"] },
  { "action": "pick_up", "parameters": ["apple"] },
  { "action": "navigate_to", "parameters": ["living room"] },
  { "action": "place_at", "parameters": ["user"] }
]
```

This structured output can then be easily parsed and executed by our Action Executor.

### Python Example

Here is a Python script that demonstrates how to use the OpenAI API to generate such a plan:

```python file=../../src/examples/vla/llm_planner.py

```

**Note**: You will need to have the `openai` Python library installed (`pip install openai`) and have an OpenAI API key set up as an environment variable or directly in the script (not recommended for production).