# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell, not on its own
'''

TodoTask = self.env['todo.task']
# retrieves a Recordset Model for the TodoTask class

TodoTask.do_clear_done()
# we call a method defined in our TodoTask class
