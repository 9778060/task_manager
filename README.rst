==========================
Task Manager Module
==========================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/License-LGPL_v3-blue.svg
    :target: https://www.gnu.org/licenses/lgpl-3.0.html
    :alt: License: LGPL-3

|badge1| |badge2|

This module allows creating and manage tasks in Odoo

Additional functionality:
* Cron job to send out email notifications when the task is due (3 days or less)
* Custom reporting on the list of tasks

**Table of contents**

.. contents::
   :local:


Installation
=====
#. Clone git hub folder task_manager into the *{Odoo folder}/server/odoo/addons/*.
#. Go to *Apps > Update Apps List* to search for the Task Manager (task_manager) module.
#. Click on *Activate* button.


Configuration
=====
#. Go to *Settings > Users & Companies > Groups*.
#. Look for the newly created group - *Task Manager User*.
#. Assign the necessary users to that group.
#. Reload the page.


Usage
=====

1. Go to the *Task Manager* menu to open a tree view of the Task Manager module.
2. A list of tasks is shown.
3. Main functionality:

   • A new task can be created using the *New* button.

   • From the tree view, an existing task can be opened and the following data can be edited:

     • **Name** — name of the task (mandatory)

     • **Description** — description of the task

     • **Assigned to** — a reference to the user assigned to the task

     • **Due date** — due date of the task (can be in the past)

     • **Priority** — priority of the task (Low, Medium, High)

     • **Status** — status of the task (New, In progress, Completed)

4. Additional functionality:

   • From the tree view, a *Print Tasks* button exports a task report into PDF:

     • If no tasks are selected, the report contains all the records.

     • If some tasks are selected, the report contains only the selected records.
     
   • A cron job sends out email notifications to the assigned user of a task.


Credits
=======

Authors
~~~~~~~

* 9778060

Maintainers
~~~~~~~~~~~

This module is maintained by the 9778060
