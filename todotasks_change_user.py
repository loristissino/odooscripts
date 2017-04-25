# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

import os

TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

user_id = int(os.getenv('ODOO_USER_ID', 0))
print "User: ", user_id
task_id = int(os.getenv('ODOO_TASK_ID', 0))
print "Task: ", task_id

try:
    task = TodoTask.browse(task_id)
    task.user_id=user_id
    print "OK - Variazione utente effettuata"
except Error as e:
    print "FAIL - Variazione utente fallita"
    
