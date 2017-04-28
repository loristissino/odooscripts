# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

last_task = TodoTask.search([], limit=1, order='create_date desc')
# retrieves the last task created

print last_task.id, last_task.name
