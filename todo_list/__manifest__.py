{
    'name': 'Todo List Management',
    'version': '1.0.0',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'summary': 'Todo List Management Module for Internal Users',
    'description': """
        Todo List Management Module
        ===========================
        
        This module provides comprehensive todo list management functionality:
        - Create, Read, Update, Delete todo lists
        - Task management with completion tracking
        - Participant management
        - Status workflow (draft -> in progress -> complete)
        - Tag system with predefined and custom tags
        - Date validation and tracking
        
        Features:
        - Internal user access with full CRUD permissions
        - Automatic status progression based on task completion
        - Inline task creation and management
        - Participant assignment from res.users
        - Three menu views: All, Uncomplete, Complete
    """,
    'author': 'Navapoom Punsathit',
    'website': 'https://github.com/NAVAPOOM/todo-list-assignment',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/todo_tags_data.xml',
        'views/todo_list_views.xml',
        'views/todo_task_views.xml',
        'views/todo_tag_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
        'demo/todo_demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
