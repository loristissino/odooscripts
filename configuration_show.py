# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

for key in odoo.tools.config.options:
    print key, '=', odoo.tools.config.options[key]


# It is possible to retrieve a specific configuration option, of course:
print
print "Database:"
print odoo.tools.config.options['log_level']

