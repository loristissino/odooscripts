# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

def print_tasks(tasks):
    for task in tasks:
        print "\t".join([str(task.id), task.name, str(task.is_done) ])
        # prints relevant info of the tasks


TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

tasks = TodoTask.search([])
# retrieves all active tasks

print "Task attivi (non eliminati)"
print_tasks(tasks)
  
tasks = TodoTask.search([ ('is_done', '=', True) ])
# retrieves current tasks (ie, not marked as done)
# see https://www.odoo.com/documentation/saas-13/reference/orm.html#domains

print "Task correnti (ancora da completare)"
print_tasks(tasks)

tasks = TodoTask.search([ ('active', '=', False) ])
# retrieves deleted tasks (ie, marked as not active)

print "Task eliminati"
print_tasks(tasks)
