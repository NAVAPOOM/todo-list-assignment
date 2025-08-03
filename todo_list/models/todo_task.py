from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'
    _order = 'sequence, id'

    name = fields.Char(
        string='Task Name',
        required=True,
        help='Name of the task'
    )
    
    description = fields.Text(
        string='Description',
        help='Detailed description of the task'
    )
    
    completed = fields.Boolean(
        string='Completed',
        default=False,
        help='Check when task is completed'
    )
    
    todo_list_id = fields.Many2one(
        'todo.list',
        string='Todo List',
        required=True,
        ondelete='cascade'
    )
    
    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help='Sequence for ordering tasks'
    )
    
    # Computed fields
    todo_list_status = fields.Selection(
        related='todo_list_id.status',
        string='Todo List Status',
        store=True
    )
    
    can_edit = fields.Boolean(
        string='Can Edit',
        compute='_compute_can_edit'
    )
    
    @api.depends('todo_list_id.status')
    def _compute_can_edit(self):
        for record in self:
            record.can_edit = record.todo_list_id.status != 'complete'
    
    def write(self, vals):
        # Prevent editing tasks when todo list is complete
        for record in self:
            if record.todo_list_id.status == 'complete':
                raise ValidationError("Cannot modify tasks in completed todo lists.")
        return super().write(vals)
    
    @api.model
    def create(self, vals):
        # Check if todo list allows new tasks
        if vals.get('todo_list_id'):
            todo_list = self.env['todo.list'].browse(vals['todo_list_id'])
            if todo_list.status == 'complete':
                raise ValidationError("Cannot add tasks to completed todo lists.")
        return super().create(vals)
