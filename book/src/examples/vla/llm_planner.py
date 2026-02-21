# This is a simplified example of how to use the OpenAI API to generate a plan.
# In a real application, you would have more robust error handling and
# a more sophisticated way of managing the conversation history.

import os
from openai import OpenAI

# It's recommended to set the API key as an environment variable.
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# For this example, we will use a placeholder.
# In a real application, DO NOT hardcode your API key.
client = OpenAI(api_key="YOUR_API_KEY_HERE")


def generate_plan(command: str, world_state: str, available_actions: list) -> str:
    """
    Generates a plan using an LLM.
    """
    prompt = f"""
You are a helpful robot assistant. Your task is to create a plan to achieve a goal.
The user's goal is: "{command}".

Current world state:
{world_state}

Available actions:
{', '.join(available_actions)}

Output the plan as a JSON array of actions.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful robot assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    user_command = "bring me the apple from the table"
    current_world_state = """
- Robot is at the charging station.
- An apple is on the kitchen table.
- The user is in the living room.
    """
    actions = ["navigate_to(location)", "pick_up(object)", "place_at(location)"]

    plan = generate_plan(user_command, current_world_state, actions)
    print(plan)
