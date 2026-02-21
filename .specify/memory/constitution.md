<!-- Sync Impact Report:
Version change: None -> 1.0.0
List of modified principles: All new
Added sections: Core Principles, Key Standards, Constraints, Success Criteria
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .claude/commands/sp.adr.md: ⚠ pending
- .claude/commands/sp.analyze.md: ⚠ pending
- .claude/commands/sp.checklist.md: ⚠ pending
- .claude/commands/sp.clarify.md: ⚠ pending
- .claude/commands/sp.constitution.md: ✅ updated (this file)
- .claude/commands/sp.git.commit_pr.md: ⚠ pending
- .claude/commands/sp.implement.md: ⚠ pending
- .claude/commands/sp.phr.md: ⚠ pending
- .claude/commands/sp.plan.md: ⚠ pending
- .claude/commands/sp.specify.md: ⚠ pending
- .claude/commands/sp.tasks.md: ⚠ pending
Follow-up TODOs: Manual review of dependent templates for alignment.
-->
# AI/Spec-driven book + integrated RAG chatbot on Physical AI & Humanoid Robotics Constitution

## Core Principles

### 1. Technical Accuracy
All technical claims, especially regarding ROS 2, Gazebo, Unity, Isaac, and VLA, must be rigorously accurate and verifiable.

### 2. Content Consistency
Book content and RAG chatbot data must maintain strict consistency to ensure a unified and reliable knowledge base.

### 3. Clear Explanations
Explanations for intermediate Python/AI learners must be clear, concise, and easy to understand, avoiding jargon where possible.

### 4. Functional & Reproducible Code
All code examples must be functional, reproducible, and accompanied by clear instructions.

### 5. Spec-Kit Plus Structure
The entire project, including the book and chatbot, must be structured and developed according to the Spec-Kit Plus methodology.

## Key Standards

### 1. Official Documentation References
All claims and technical details must reference official documentation from sources like ROS 2, Gazebo, Isaac, and OpenAI SDKs.

### 2. Code Conventions
Code must strictly adhere to established conventions for ROS 2 (rclpy), FastAPI, and OpenAI Chat/Agents.

### 3. Docusaurus v3 & Clean Builds
The book must utilize Docusaurus v3 for documentation, ensuring clean builds and proper formatting.

### 4. Context-Grounded RAG
The RAG chatbot must strictly answer questions based on retrieved context, avoiding hallucination or external knowledge.

### 5. Qdrant + Neon Postgres Defaults
Qdrant and Neon Postgres setups must follow all recommended default configurations for optimal performance and stability.

## Constraints

### 1. Book Chapter Length
The book must contain 8–12 chapters, with each chapter ranging from 1.5–3k words.

### 2. Code Example Count
The project must include at least 40 code examples across all modules.

### 3. GitHub Pages Deployment
The book must be deployable and accessible via GitHub Pages.

### 4. Chatbot Modes
The chatbot must support the following modes: full-book Q/A, section-specific Q/A, and highlight-based Q/A.

### 5. Diagram Format
All diagrams used in the project must be in SVG format.

## Success Criteria

### 1. Error-Free GitHub Pages Deployment
The book must deploy on GitHub Pages without any errors.

### 2. Context-Grounded RAG Answers
The RAG chatbot must consistently provide answers that are strictly grounded in the provided context, demonstrating no evidence of hallucination.

## Governance

### 1. Amendment Procedure
Amendments to this constitution require documentation, approval from the project lead, and a clear migration plan for any affected components.

### 2. Versioning Policy
This constitution follows semantic versioning (MAJOR.MINOR.PATCH). Major versions indicate backward-incompatible changes to core principles. Minor versions indicate new principles or significantly expanded guidance. Patch versions are for clarifications, wording fixes, and non-semantic refinements.

### 3. Compliance Review
All pull requests and code reviews must verify compliance with the principles and standards outlined in this constitution.

**Version**: 1.0.0 | **Ratified**: 2025-12-12 | **Last Amended**: 2025-12-12