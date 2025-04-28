from odoo import models, fields, api, http
from datetime import datetime
import logging


_logger = logging.getLogger(__name__)


class TaskManager(models.Model):
    """Model for the Task manager module"""
    _name = "task.manager"
    _description = "Task Manager"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    assigned_to = fields.Many2one("res.users", string="Assigned To")
    due_date = fields.Datetime(string="Due Date")
    priority = fields.Selection([
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ], string="Priority", default="medium")
    status = fields.Selection([
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("completed", "Completed")
    ], string="Status", default="new")

    def _calculate_days_left(task):
        """Supplementary function to calculate number of days left until the due date.
        
        Positional arguments:
        task -- a Task Manager instance

        Returns:
        Either number of days due (positive values); in case of negative value a 0 is returned
        Or
        None if there is no Due date given
        """

        # trying to convert date from string and calculate number of days left for the task
        try:
            due_date = fields.Datetime.from_string(task.due_date)
            days_left = (due_date - datetime.now()).days

            _logger.info("Unabriged calculated number of days left %s for task %s", days_left, task.id)

            return max(0, days_left)
        except Exception:
            return None

    def send_task_expiry_email(self):
            """Sends an email to the assigned user if the task is about to expire (3 days before due date or less)."""

            # checking whether there is a due date present and status of the task is not completed
            for task in self.search([("due_date", "!=", False), ("status", "!=", "completed")]):
                days_left = TaskManager._calculate_days_left(task)

                _logger.info("Calculated number of days left %s for task %s", days_left, task.id)

                # if days left are still present and due date is not far in the future
                if days_left is not None and days_left <= 3:
                        
                        # getting email template
                        template = self.env.ref("task_manager.email_template_task_expiry")
                        template.with_context(days_left=days_left).send_mail(task.id, force_send=True)
                        
                        _logger.info("Email for task %s has been sent", task.id)


class ReportTaskManagerList(models.AbstractModel):
    """Model for the Task manager report. Overriding get values function
    
    To return either selected records
    Or
    All records (if none selected)
    """
    _name = "report.task_manager.report_task_manager_list"
    _description = "Task Manager List"
    
    @api.model
    def _get_report_values(self, docids, data=None):
        if not docids:
            # If no specific record is selected, return all tasks
            task_managers = self.env["task.manager"].search([])
            _logger.info("All the records to be extracted in the output report")
        else:
            task_managers = self.env["task.manager"].browse(docids)
            _logger.info("Only selected records to be extracted in the output report: %s", docids)
        
        return {
            "docs": task_managers,
        }
