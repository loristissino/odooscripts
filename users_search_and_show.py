# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

UserModel = self.env['res.users']
# retrieves a Recordset Model for the User class

users = UserModel.search([])
# retrieves all active users

for user in users:
    print "\t".join([str(user.id), user.name ])
