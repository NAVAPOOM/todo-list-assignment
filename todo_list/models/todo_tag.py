from odoo import models, fields

class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'
    _order = 'name'

    name = fields.Char(
        string='Tag Name',
        required=True,
        help='Name of the tag'
    )
    
    color = fields.Integer(
        string='Color',
        help='Color for the tag'
    )
    
    description = fields.Text(
        string='Description',
        help='Description of the tag'
    )
    
    todo_list_ids = fields.Many2many(
        'todo.list',
        string='Todo Lists',
        help='Todo lists using this tag'
    )
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tag name must be unique!')
    ]
