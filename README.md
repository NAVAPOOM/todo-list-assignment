# Todo List Management Module for Odoo

This module provides a comprehensive system for managing todo lists within Odoo, designed for internal users to track tasks, projects, and personal goals.

## Overview

The "Todo List Management" module allows users to create, organize, and track various todo lists. Each todo list can have multiple tasks, assigned participants, and be categorized using tags. It supports a clear workflow from draft to completion, with progress tracking for tasks.

## Features

- **Todo List Management**:
  - Create, view, edit, and delete todo lists.
  - Each list includes a title, start date, end date, and status.
  - Automatic calculation of task progress percentage.
  - Ability to mark a todo list as "In Progress" from "Draft".
  - Ability to mark a todo list as "Complete" once all tasks are finished.
  - Prevents editing of completed todo lists.

- **Task Management**:
  - Add multiple tasks to each todo list.
  - Each task has a name, description, and completion status.
  - Tasks can be marked as completed.
  - Tasks cannot be added or modified if the parent todo list is "Complete".

- **Tagging System**:
  - Categorize todo lists using predefined tags (e.g., Work, Event, Life achievement).
  - Users can also add custom tags.

- **Participant Management**:
  - Assign Odoo users as participants to a todo list.

- **Status Workflow**:
  - **Draft**: Initial state, can be edited.
  - **In Progress**: Actively working on the list, tasks can be completed.
  - **Complete**: All tasks are done, the list is finalized and becomes read-only.

- **Reporting & Views**:
  - **List View**: Displays all todo lists with key information like title, dates, status, participants, and progress.
  - **Form View**: Detailed view for creating and editing todo lists, including sections for basic info, tags, participants, and tasks.
  - **Search & Filters**: Easily find todo lists by title, tags, participants, or status (Draft, In Progress, Complete, Uncomplete, My Todo Lists).
  - **Group By**: Group todo lists by status, start date, or tags.

## Installation

1. **Clone/Download** this module into your Odoo `addons` path.
2. **Restart** your Odoo server.
3. Go to the **Apps** menu in Odoo.
4. Click on **Update Apps List** (if you don't see the module).
5. Search for **Todo List Management** and click the **Install** button.

## Usage

After installation, you can access the module from the main Odoo menu:

1. Navigate to **Todo Lists** in the main menu.
2. You will see sub-menus for:
   - **All**: View all todo lists.
   - **Uncomplete**: View todo lists that are still in "Draft" or "In Progress" status.
   - **Complete**: View todo lists that have been marked as "Complete".
   - **Configuration > Tags**: Manage the tags used for todo lists.
3. Click **Create** to add a new todo list and fill in the required details.
4. Within a todo list, you can add tasks, assign participants, and update its status.
5. Use the **Start Progress** button to move a list from "Draft" to "In Progress".
6. Once all tasks are completed, the **Mark Complete** button will become available to finalize the list.

## Module Structure

- `__manifest__.py`: Module manifest file, defining metadata and dependencies.
- `__init__.py`: Python initialization file for the module.
- `models/`: Contains Python models (`todo_list.py`, `todo_task.py`, `todo_tag.py`) defining the data structures and business logic.
- `security/`: Defines access rights (`ir.model.access.csv`).
- `data/`: Contains initial data, such as default tags (`todo_tags_data.xml`).
- `views/`: Contains XML files defining the user interface views (list, form, search) for todo lists, tasks, and tags, as well as menu items.
- `demo/`: Contains demo data for testing purposes (`todo_demo_data.xml`).
