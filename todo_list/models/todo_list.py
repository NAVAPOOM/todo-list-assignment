from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'
    _rec_name = 'title'

    title = fields.Char(
        string='Title',
        required=True,
        help='Todo list title - must be specified'
    )
    
    tag_ids = fields.Many2many(
        'todo.tag',
        string='Tags',
        help='Tags for categorizing todo lists'
    )
    
    start_date = fields.Date(
        string='Start Date',
        required=True,
        default=fields.Date.context_today,
        help='Start date - must be specified'
    )
    
    end_date = fields.Date(
        string='End Date',
        required=True,
        help='End date - must be specified and greater than start date'
    )
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], string='Status', default='draft', required=True, tracking=True)
    
    participant_ids = fields.Many2many(
        'res.users',
        string='Participants',
        help='Users participating in this todo list'
    )
    
    task_ids = fields.One2many(
        'todo.task',
        'todo_list_id',
        string='Tasks'
    )
    
    # Computed fields
    task_count = fields.Integer(
        string='Total Tasks',
        compute='_compute_task_stats',
        store=True
    )
    
    completed_task_count = fields.Integer(
        string='Completed Tasks',
        compute='_compute_task_stats',
        store=True
    )
    
    progress_percentage = fields.Float(
        string='Progress %',
        compute='_compute_task_stats',
        store=True
    )
    
    all_tasks_completed = fields.Boolean(
        string='All Tasks Completed',
        compute='_compute_task_stats',
        store=True
    )
    
    can_mark_complete = fields.Boolean(
        string='Can Mark Complete',
        compute='_compute_can_mark_complete'
    )
    
    @api.depends('task_ids.completed')
    def _compute_task_stats(self):
        for record in self:
            total_tasks = len(record.task_ids)
            completed_tasks = len(record.task_ids.filtered('completed'))
            
            record.task_count = total_tasks
            record.completed_task_count = completed_tasks
            
            if total_tasks > 0:
                record.progress_percentage = (completed_tasks / total_tasks) * 100
                record.all_tasks_completed = (completed_tasks == total_tasks)
            else:
                record.progress_percentage = 0.0
                record.all_tasks_completed = False
    
    @api.depends('status', 'all_tasks_completed', 'task_count')
    def _compute_can_mark_complete(self):
        for record in self:
            record.can_mark_complete = (
                record.status == 'in_progress' and 
                record.all_tasks_completed and 
                record.task_count > 0
            )
    
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date <= record.start_date:
                    raise ValidationError("End date must be greater than start date.")
    
    @api.constrains('status')
    def _check_status_transition(self):
        for record in self:
            if record.status == 'complete':
                # Once complete, cannot be changed
                pass
    
    def action_start_progress(self):
        """Change status from draft to in progress"""
        for record in self:
            if record.status == 'draft':
                record.status = 'in_progress'
        return True
    
    def action_mark_complete(self):
        """Mark todo list as complete when all tasks are done"""
        for record in self:
            if record.can_mark_complete:
                record.status = 'complete'
        return True
    
    def action_view_tasks(self):
        """Action to view tasks of this todo list"""
        return {
            'name': 'Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'todo.task',
            'view_mode': 'tree,form',
            'domain': [('todo_list_id', '=', self.id)],
            'context': {'default_todo_list_id': self.id},
        }
    
    def write(self, vals):
        # Prevent editing when status is complete
        for record in self:
            if record.status == 'complete' and any(key != 'status' for key in vals.keys()):
                raise ValidationError("Cannot modify completed todo lists. You can only view them.")
        return super().write(vals)
    
    @api.model
    def create(self, vals):
        # Set default tags if none provided
        if not vals.get('tag_ids'):
            default_tag = self.env['todo.tag'].search([('name', '=', 'Work')], limit=1)
            if default_tag:
                vals['tag_ids'] = [(6, 0, [default_tag.id])]
        return super().create(vals)
