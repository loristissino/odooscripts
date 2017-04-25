# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell,
not on its own
'''

Attachment = self.env['ir.attachment']
# retrieves a Recordset Model for the Attachment class

for attachment in Attachment.search([]):
    print attachment.store_fname, attachment.mimetype, attachment.datas_fname, attachment.file_size
