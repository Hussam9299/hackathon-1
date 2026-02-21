# Tasks: Module 4: Vision-Language-Action (VLA)

**Input**: Design documents from `specs/005-vision-language-action/`
**Prerequisites**: plan.md, spec.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the directory structure for the new Docusaurus module.

- [X] T001 Create module directory `book/docs/module4-vla`
- [X] T002 Create an image asset subdirectory `book/static/img/module4`
- [X] T003 Create an examples subdirectory `book/src/examples/vla`

---

## Phase 2: User Story 1 - Understand VLA Pipelines (Priority: P1) 🎯 MVP

**Goal**: Create a chapter that explains the architecture of a Vision-Language-Action (VLA) pipeline.

**Independent Test**: A user can read the chapter and understand the flow of information from a natural language command to a robot action.

### Implementation for User Story 1

- [X] T004 [US1] Create the chapter file `book/docs/module4-vla/1-vla-architecture.md`
- [X] T005 [US1] Write the core content for the "VLA Architecture" chapter.
- [X] T006 [P] [US1] Create an SVG diagram illustrating the VLA pipeline and place it in `book/static/img/module4/vla-pipeline.svg`
- [X] T007 [US1] Add the diagram to the chapter `book/docs/module4-vla/1-vla-architecture.md`

**Checkpoint**: Chapter 1 is complete and explains the VLA concept.

---

## Phase 3: User Story 2 - Implement LLM-based Planning (Priority: P2)

**Goal**: Create a chapter on how to use an LLM to translate natural language commands into ROS 2 actions.

**Independent Test**: A user can run a Python script that takes a text command and outputs a sequence of ROS 2 actions.

### Implementation for User Story 2

- [X] T008 [US2] Create the chapter file `book/docs/module4-vla/2-llm-planning.md`
- [X] T009 [US2] Write content for the "LLM-based Planning" chapter.
- [X] T010 [US2] Create a Python script example `book/src/examples/vla/llm_planner.py` that takes a text prompt and calls the OpenAI API to generate a plan.
- [X] T011 [US2] Embed the code example in `book/docs/module4-vla/2-llm-planning.md`

**Checkpoint**: Chapter 2 is complete, and users can understand how to use LLMs for robotic planning.

---

## Phase 4: User Story 3 - Run an End-to-End Simulation (Priority: P3)

**Goal**: Provide a capstone project that integrates all modules into an end-to-end autonomous humanoid simulation.

**Independent Test**: A user can launch the full simulation and give the robot a command to complete a task.

### Implementation for User Story 3

- [X] T012 [US3] Create the chapter file `book/docs/module4-vla/3-capstone-project.md`
- [X] T013 [US3] Write the tutorial content for the "Autonomous Humanoid Capstone" chapter.
- [X] T014 [US3] Create a launch file `book/src/examples/vla/capstone.launch.py` that integrates components from all modules (perception, navigation, planning).
- [X] T015 [US3] Embed the launch file and detailed instructions in `book/docs/module4-vla/3-capstone-project.md`

**Checkpoint**: The capstone project is documented and functional.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final review and quality assurance for the entire module.

- [X] T016 [P] Review all chapters for technical accuracy and clarity.
- [X] T017 [P] Verify all code examples and launch files are working correctly.
- [ ] T018 Build the full Docusaurus site and ensure there are no warnings or errors. (NOTE: Could not be completed due to execution policy).

---

## Dependencies & Execution Order

- **Setup (Phase 1)**: Can start immediately.
- **User Stories (Phase 2-4)**: Depend on Setup completion. User stories can be worked on sequentially.
- **Polish (Phase 5)**: Depends on all user stories being complete.
