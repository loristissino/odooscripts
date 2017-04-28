# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

for i in range(10):
    newtask = TodoTask.create( { 'name': 'New task %03d' % i } )
    newtask.is_done = i % 2 == 0
    # we create half of the tasks as done
