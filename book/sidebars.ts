import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: ROS 2',
      items: [
        'module1-ros2/chapter1-concepts',
        'module1-ros2/chapter2-python-examples',
        'module1-ros2/chapter3-urdf-modeling',
        'module1-ros2/chapter4-launch-files',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin',
      items: [
        'module2-digital-twin/chapter1-gazebo-simulation',
        'module2-digital-twin/chapter2-unity-digital-twin',
        'module2-digital-twin/chapter3-sensor-simulation',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: NVIDIA Isaac',
      items: [
        'module3-nvidia-isaac/introduction-to-isaac-sim',
        'module3-nvidia-isaac/perception-with-isaac-ros',
        'module3-nvidia-isaac/navigation-with-nav2',
      ],
    },
    {
        type: 'category',
        label: 'Module 4: VLA',
        items: [
          'module4-vla/vla-architecture',
          'module4-vla/llm-planning',
          'module4-vla/capstone-project',
        ],
      },
  ],
};

export default sidebars;