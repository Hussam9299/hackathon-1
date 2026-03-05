import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A book on building intelligent robots',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://hackathon-1-taupe.vercel.app/',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Hussam9299', // Usually your GitHub org/user name.
  projectName: 'hackathon-1', // Usually your repo name.

  onBrokenLinks: 'throw',

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },
  themes: ['@docusaurus/theme-mermaid'],

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Hussam9299/hackathon-1/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Modules',
        },
        {
          href: 'https://github.com/Hussam9299/hackathon-1',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Module 1: ROS 2',
          items: [
            {
              label: 'Concepts',
              to: '/docs/module1-ros2/chapter1-concepts',
            },
            {
              label: 'Python Examples',
              to: '/docs/module1-ros2/chapter2-python-examples',
            },
            {
              label: 'URDF Modeling',
              to: '/docs/module1-ros2/chapter3-urdf-modeling',
            },
            {
              label: 'Launch Files',
              to: '/docs/module1-ros2/chapter4-launch-files',
            },
          ],
        },
        {
          title: 'Module 2: Digital Twin',
          items: [
            {
              label: 'Gazebo Simulation',
              to: '/docs/module2-digital-twin/chapter1-gazebo-simulation',
            },
            {
              label: 'Unity Digital Twin',
              to: '/docs/module2-digital-twin/chapter2-unity-digital-twin',
            },
            {
              label: 'Sensor Simulation',
              to: '/docs/module2-digital-twin/chapter3-sensor-simulation',
            },
          ],
        },
        {
          title: 'Module 3: NVIDIA Isaac',
          items: [
            {
              label: 'Intro to Isaac Sim',
              to: '/docs/module3-nvidia-isaac/introduction-to-isaac-sim',
            },
            {
              label: 'Perception (Isaac ROS)',
              to: '/docs/module3-nvidia-isaac/perception-with-isaac-ros',
            },
            {
              label: 'Navigation (Nav2)',
              to: '/docs/module3-nvidia-isaac/navigation-with-nav2',
            },
          ],
        },
        {
          title: 'Module 4: VLA',
          items: [
            {
              label: 'VLA Architecture',
              to: '/docs/module4-vla/vla-architecture',
            },
            {
              label: 'LLM Planning',
              to: '/docs/module4-vla/llm-planning',
            },
            {
              label: 'Capstone Project',
              to: '/docs/module4-vla/capstone-project',
            },
          ],
        },
        {
          title: 'Community & More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/Hussam9299/hackathon-1',
            },
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
