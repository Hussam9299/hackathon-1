# hackathon-1 Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-13

## Active Technologies
- Gazebo Fortress, Unity 2021 LTS, Python 3.8+ + Docusaurus v3, Gazebo, Unity, ROS 2 Humble/Foxy (003-digital-twin-simulation)

- NVIDIA Isaac Sim, Isaac ROS, Nav2, Python 3.8+ + Docusaurus v3, ROS 2 Humble/Foxy (004-nvidia-isaac-brain)

- OpenAI API, Python 3.8+ + Docusaurus v3, ROS 2 Humble/Foxy (005-vision-language-action)

- Python 3.8+ (for ROS 2 Humble/Foxy) + Docusaurus v3, ROS 2 Humble/Foxy, rclpy (1-ros2-control-module)

- Cohere, Qdrant, uv, Python 3.8+ (6-embedding-ingestion-pipeline)

## Project Structure

```text
book/
├── docs/
│   ├── module1-ros2/
│   │   ├── chapter1.md
│   │   └── _category_.json
│   └── intro.md
├── src/
│   ├── css/
│   │   └── custom.css
│   └── pages/
│       └── index.js
├── static/
│   └── img/
├── docusaurus.config.js
└── package.json
```

## Commands

cd src; pytest; ruff check .

## Code Style

Python 3.8+ (for ROS 2 Humble/Foxy): Follow standard conventions

## Recent Changes
- 003-digital-twin-simulation: Added Gazebo Fortress, Unity 2021 LTS, Python 3.8+ + Docusaurus v3, Gazebo, Unity, ROS 2 Humble/Foxy

- 004-nvidia-isaac-brain: Added NVIDIA Isaac Sim, Isaac ROS, Nav2

- 005-vision-language-action: Added OpenAI API

- 1-ros2-control-module: Added Python 3.8+ (for ROS 2 Humble/Foxy) + Docusaurus v3, ROS 2 Humble/Foxy, rclpy

- 6-embedding-ingestion-pipeline: Added Cohere, Qdrant, uv

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
