# GDSC Kanband Board
### this is a submission for the 2024 enrollment for GDSC culb.

# Kanban Board Application

The Kanban Board Application is a command-line tool built using the Python `curses` library. It provides a visual representation of a Kanban board, allowing users to manage tasks and organize their workflow.

## Features

- **Task Management**: The application allows users to create, edit, and delete tasks within the Kanban board.
- **Task Prioritization**: Users can assign different priority levels (High, Medium, Low) to their tasks.
- **Task Assignment**: Users can assign tasks to specific individuals and report to others.
- **Task Description**: Users can add a description for each task.
- **Sections**: The application provides three default sections: "TODO", "IN PROGRESS", and "DONE". Users can also create additional custom sections.
- **Mouse Interaction**: The application supports mouse interactions, allowing users to add new tasks and sections by clicking on the designated areas.

## Usage

1. Run the `main()` function to start the application.
2. The application will display the Kanban board with the default sections.
3. To add a new task, click on the "+ Add task" button in the desired section.
4. Fill in the task details, including priority, assigned to, reported to, and description.
5. To delete a task, click on the "x" button in the top-right corner of the task window.
6. To create a new section, click on the "+" button in the top-right corner of the board.
7. To quit the application, press the "q" key.

## Code Structure

The application consists of the following main components:

1. `section` class: Represents a section of the Kanban board, handling the creation and management of tasks within the section.
2. `task` class: Represents a task within the Kanban board, handling the creation and management of task details.
3. `kanban` class: Manages the overall Kanban board, including the title, author, and date.
4. `initialize(window)` function: Initializes the Kanban board and sets up the default sections.
5. `add_task(section, max_lines)` function: Adds a new task to the specified section.
6. `del_task(section_id, task_id)` function: Removes a task from the specified section.
7. `mouse_event(x, y, max_lines, max_cols)` function: Handles mouse interactions, such as adding new tasks and sections.
8. `c_main(stdscr)` function: The main entry point of the application, which sets up the `curses` environment and handles the main loop.

## Dependencies

- Python 3.x
- `curses` library (part of the Python standard library)

## Future Improvements

- Add support for saving and loading Kanban boards to/from a file.
- Implement drag-and-drop functionality for tasks between sections.
- Enhance the user interface with more visual elements and color schemes.
- Add keyboard shortcuts for common actions.
- Implement user authentication and collaborative features.
