# Research for "Physical AI & Humanoid Robotics" Book

This document outlines the high-level technical and structural decisions for the entire book project.

## 1. Docusaurus Configuration

### Decision
- **Docusaurus Version**: Docusaurus v3.
- **Theme**: The `'classic'` preset will be used.
- **Plugins**: No additional plugins are required at this stage. The default plugins from the classic preset are sufficient.

### Rationale
- The project is already using Docusaurus v3 with the classic theme. Sticking with this ensures consistency and avoids rework. The classic preset provides all the necessary features for a documentation website, including docs, MDX support, and theming.

## 2. Module Sequencing and Chapter Granularity

### Decision
- **Module Sequence**: The modules will be ordered logically to build knowledge progressively:
    1.  Module 1: ROS 2 Control
    2.  Module 2: Digital Twin Simulation
    3.  Module 3: AI-Robot Brain (NVIDIA Isaac)
    4.  Module 4: Vision-Language-Action (VLA)
- **Chapter Granularity**: Each module will consist of 2-4 chapters, with each chapter focusing on a specific, digestible topic.

### Rationale
- This sequence starts with the fundamentals of ROS 2, moves to creating simulated environments, then covers advanced perception, and finally integrates everything into an intelligent, end-to-end system. This provides a clear learning path for the reader.

## 3. Sidebar, Navigation, and Versioning

### Decision
- **Sidebar**: The sidebar will be auto-generated from the file system, as is the current setup in `sidebars.ts`.
- **Navigation**: The primary navigation will be through the sidebar. A top navbar will provide a link to the main modules page.
- **Versioning**: Documentation versioning will not be implemented initially but can be enabled later if the book requires major revisions.

### Rationale
- Auto-generated sidebars are easy to maintain. The directory structure will dictate the sidebar structure. This approach is simple and effective for a project of this scale.

## 4. Content Standards

### Decision
- **Markdown**: All content will be written in Docusaurus-flavored Markdown (MDX).
- **Code Blocks**: All code blocks must include a language specifier.
- **Diagrams**: All diagrams must be in SVG format.

### Rationale
- These standards are consistent with Docusaurus best practices and ensure a high-quality, uniform presentation of the content.

## 5. GitHub Pages Deployment and CI Workflow

### Decision
- **Deployment**: The book will be deployed to GitHub Pages.
- **CI Workflow**: A GitHub Actions workflow will be set up to automatically build and deploy the Docusaurus site on every push to the `main` branch.

### Rationale
- This automates the deployment process, ensuring that the live book is always up-to-date with the latest content.

## 6. LLM API Choice

### Decision
- **LLM API**: The project will use the **OpenAI API** for the VLA module.

### Rationale
- The OpenAI API is well-documented, widely used, and provides powerful models suitable for the cognitive planning tasks required in the VLA module. It has robust client libraries in Python, which aligns with the project's tech stack.
