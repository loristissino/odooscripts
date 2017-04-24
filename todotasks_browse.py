# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

TodoTask.browse(17).do_toggle_done()
# we call a method defined in our TodoTask class on the
# specific task (with id=17)

TodoTask.browse(range(18, 22)).do_toggle_done()
# we call a method defined in our TodoTask class on the
# specific tasks (with id in the range from 18 to 21 included)
