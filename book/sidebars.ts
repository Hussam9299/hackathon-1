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
        'module3-nvidia-isaac/1-introduction-to-isaac-sim',
        'module3-nvidia-isaac/2-perception-with-isaac-ros',
        'module3-nvidia-isaac/3-navigation-with-nav2',
      ],
    },
    {
        type: 'category',
        label: 'Module 4: VLA',
        items: [
          'module4-vla/1-vla-architecture',
          'module4-vla/2-llm-planning',
          'module4-vla/3-capstone-project',
        ],
      },
  ],
};

export default sidebars;