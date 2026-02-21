---
sidebar_position: 2
---

# Chapter 2: Your First ROS 2 Nodes in Python

In the previous chapter, we learned about the fundamental concepts of ROS 2. Now, it's time to put that knowledge into practice by creating our first ROS 2 nodes using Python. We'll build a simple publisher and subscriber to see how they communicate with each other.

## The Publisher Node

Let's start with the publisher. This node will publish a "Hello World" message to a topic every half a second.

Create a file named `publisher.py` with the following content:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldPublisher(Node):

    def __init__(self):
        super().__init__('hello_world_publisher')
        self.publisher_ = self.create_publisher(String, 'hello_world', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    hello_world_publisher = HelloWorldPublisher()
    rclpy.spin(hello_world_publisher)
    hello_world_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Code Explained

- We import the necessary libraries: `rclpy`, `Node`, and `String`.
- We create a `HelloWorldPublisher` class that inherits from `Node`.
- In the `__init__` method, we call the parent constructor, create a publisher, and set up a timer to call the `timer_callback` method every 0.5 seconds.
- The `timer_callback` method creates a `String` message, publishes it to the `hello_world` topic, and logs the message to the console.
- The `main` function initializes ROS 2, creates an instance of our publisher, and then `spins` the node, which keeps it running until it's shut down.

## The Subscriber Node

Now let's create the subscriber. This node will subscribe to the `hello_world` topic and print any messages it receives.

Create a file named `subscriber.py` with the following content:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldSubscriber(Node):

    def __init__(self):
        super().__init__('hello_world_subscriber')
        self.subscription = self.create_subscription(
            String,
            'hello_world',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    hello_world_subscriber = HelloWorldSubscriber()
    rclpy.spin(hello_world_subscriber)
    hello_world_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Code Explained

- The subscriber code is similar to the publisher.
- In the `__init__` method, we create a subscription to the `hello_world` topic. We also specify the message type (`String`) and a callback function (`listener_callback`) to be executed whenever a message is received.
- The `listener_callback` function simply logs the received message to the console.

## Running the Nodes

To see these nodes in action, you'll need to run them in separate terminals.

First, make sure you have sourced your ROS 2 environment:

```bash
# For Humble
source /opt/ros/humble/setup.bash

# For Foxy
source /opt/ros/foxy/setup.bash
```

**Terminal 1: Run the Publisher**

In your first terminal, navigate to the `book/src/examples/ros2` directory and run the publisher node:

```bash
python publisher.py
```

You should see output like this:

```
[INFO] [hello_world_publisher]: Publishing: "Hello World: 0"
[INFO] [hello_world_publisher]: Publishing: "Hello World: 1"
[INFO] [hello_world_publisher]: Publishing: "Hello World: 2"
...
```

**Terminal 2: Run the Subscriber**

In your second terminal, navigate to the same directory and run the subscriber node:

```bash
python subscriber.py
```

You should see output like this:

```
[INFO] [hello_world_subscriber]: I heard: "Hello World: 0"
[INFO] [hello_world_subscriber]: I heard: "Hello World: 1"
[INFO] [hello_world_subscriber]: I heard: "Hello World: 2"
...
```

Congratulations! You have successfully created and run your first ROS 2 publisher and subscriber. You can see the nodes communicating with each other in real-time.

## Bridging Python Agents to ROS Controllers

A powerful application of ROS 2 is its ability to interface with other Python applications. For example, a Python-based AI agent (like the one writing this book!) can interact with a ROS 2 system to control a robot.

The key is to use the same communication mechanisms we've already learned about: topics and services.

### Conceptual Example

Imagine you have a Python agent that decides a robot should move forward. The agent can publish a message to a ROS 2 topic that a motor controller node is subscribed to.

Here is a pseudo-code example of what this might look like from the agent's perspective:

```python
# This is not a ROS 2 node, but a regular Python script
import rclpy
from std_msgs.msg import String

# A simplified function to publish a single message
def send_command_to_ros(command):
    rclpy.init()
    # Create a temporary node to send the message
    node = rclpy.create_node('agent_bridge')
    publisher = node.create_publisher(String, 'robot_commands', 10)
    msg = String()
    msg.data = command
    publisher.publish(msg)
    # Clean up
    node.destroy_node()
    rclpy.shutdown()

# The agent's main logic
def agent_logic():
    # ... some complex decision making ...
    if should_move_forward():
        send_command_to_ros('forward')

```

In this conceptual example, the Python agent uses the `rclpy` library to create a temporary node and publish a command to a ROS 2 topic. A separate ROS 2 node running on the robot would subscribe to this topic and execute the command.

This demonstrates how ROS 2 can serve as a bridge between high-level AI and low-level robot control, which is a central theme of this book.


