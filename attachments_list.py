# -*- coding: utf-8 -*-

'''
This script is meant to be executed inside the odoo shell, not on its own
'''

Attachment = self.env['ir.attachment']
# retrieves a Recordset Model for the Attachment class

for attachment in Attachment.search([('res_model', '!=', False)]):
    print "\t".join([
        attachment.store_fname,
        attachment.mimetype,
        attachment.datas_fname,
        str(attachment.file_size),
        attachment.res_model
        ])

print "Files are stored in %s/filestore/%s" % (
    odoo.tools.config.options['data_dir'], odoo.tools.config.options['db_name']
    )
