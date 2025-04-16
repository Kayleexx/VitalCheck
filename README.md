# VitalCheck: Your pookie health consultant 🎀
VitalCheck is an advanced system designed to facilitate seamless collaboration among multiple agents for achieving complex tasks. This project, developed as part of the Scrapybara Bounty Force submission, emphasizes modular design, robust error handling, and user-centric functionality to deliver a reliable, scalable solution.

---

## Features

The **VitalCheck** includes the following robust features:

### 1. **Error Handling**
- Comprehensive exception handling with proper propagation.
- Retry mechanism for managing agent lifecycle issues.
- Exponential backoff implemented in `AgentManager`.

### 2. **State Management**
- Utilizes an `AgentState` dataclass to track agent statuses efficiently.
- Robust lifecycle management for agents, ensuring proper initialization and termination.
- Improved resource cleanup to prevent memory leaks and optimize performance.

### 3. **Modular Design**
- Separation of concerns for each module to simplify development and testing.
- Each module follows the **Single Responsibility Principle**, ensuring clarity and maintainability.

### 4. **Type Annotations**
- Extensive use of type hints for enhanced code clarity.
- Reduces debugging time by catching type-related errors during development.

### 5. **Advanced Logging**
- Centralized logging system with configurable settings.
- Logs are directed to both console and files, offering real-time and persistent records.
- Log levels include `INFO`, `DEBUG`, `WARNING`, `ERROR`, and `CRITICAL`.

---

## Project Architecture

This project adheres to a well-defined modular structure, ensuring a clear separation of responsibilities. Below is the high-level overview:

### Directory Structure
```
collaborative_agents/
│
├── env/                     # Virtual environment folder
├── logs/                    # Directory for log files
├── health_consultant.py     # Main entry point
├── agent_manager.py         # Manages agent lifecycle and states
├── user_interface.py        # Manages user interactions
├── report_generator.py      # Generates and saves reports
├── config.py                # Handles configuration loading
├── .env                     # Environment variables
└── README.md                # Documentation
```

---

## Usage

1. **Interactive User Interface**:
   - Launch the application to access an intuitive UI for managing agents.
   - Input tasks and manage configurations via prompts.

2. **Agent Collaboration**:
   - Agents work collaboratively to perform tasks, leveraging modular logic.
   - Monitor progress through real-time logs.

3. **Generate Reports**:
   - Upon task completion, detailed reports are generated and saved.
   - Reports include task summaries, agent performance, and error logs.

---

## Modules Overview

### 1. `health_consultant.py`
- Orchestrates the entire workflow.
- Coordinates communication between modules.
- Acts as the main entry point for the application.

### 2. `agent_manager.py`
- Handles agent initialization, execution, and termination.
- Implements retry mechanisms with exponential backoff.
- Tracks agent states using the `AgentState` dataclass.

### 3. `user_interface.py`
- Manages all user interactions.
- Provides prompts for input and displays feedback.
- Ensures a seamless user experience.

### 4. `report_generator.py`
- Generates structured reports based on task results.
- Saves reports in a user-friendly format (e.g., `.txt`, `.pdf`).

### 5. `config.py`
- Loads configuration settings from `.env` and other sources.
- Provides a centralized configuration management system.

---

## Logging

- **Log Location**: All logs are saved in the `logs/` directory.
- **Log Levels**:
  - `INFO`: General workflow updates.
  - `DEBUG`: Detailed system diagnostics.
  - `WARNING`: Potential issues requiring attention.
  - `ERROR`: Critical failures.
  - `CRITICAL`: Severe system errors.

Example log snippet:
```
2024-12-30 12:00:00,123 - agent_manager - INFO - Agent initialized successfully.
2024-12-30 12:01:00,456 - agent_manager - ERROR - Agent failed to respond. Retrying...
```

---

## Error Handling and State Management

- Implements robust exception handling to ensure smooth execution.
- Tracks agent states (e.g., `Initialized`, `Running`, `Failed`, `Completed`) using the `AgentState` dataclass.
- Ensures proper cleanup of resources upon errors or termination.

---


## Demo
[![Watch the video](https://imgur.com/a/fEJstYn)](https://drive.google.com/file/d/1_5kJtZru3suSxdWCGwV7HtMpb7jviLfX/view?usp=sharing) 

