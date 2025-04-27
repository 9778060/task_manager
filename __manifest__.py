# A manifest with the main App parameters
{
    "name": "Task Manager",
    "version": "1.0",
    "category": "Productivity",
    "summary": "Manage your tasks easily",
    "author": "Your Name",
    "license": "LGPL-3",
    "depends": ["base", "mail"],    # dependencies: base and for emails
    "data": [
        "security/security.xml",    # a new user group to be able to use the app
        "security/ir.model.access.csv", # access rights for the created user group
        "views/task_manager_views.xml", # form, tree views and menus
        "data/task_manager_cron.xml",   # cron job configuration
        "data/task_manager_email_template.xml", # email template
        "report/task_manager_report.xml",   # report action
        "report/task_manager_report_templates.xml",  # report template
    ],
    "installable": True,
    "application": True,
}