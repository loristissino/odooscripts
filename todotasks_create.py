# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

for i in range(10):
    is_done = i % 2 == 0
    # we create half of the tasks as done
    newtask = TodoTask.create( { 'name': 'New task %03d' % i, 'is_done': is_done } )
    print "created task, id=", newtask.id

# self.env.cr.commit()
# to make the changes persistent, uncomment the preceding line,
# that should be the last instruction executed
