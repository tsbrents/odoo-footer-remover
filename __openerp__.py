# -*- coding: utf-8 -*-
{
    'name': "footer_remover",

    'summary': """
       This module removes the default email footer on outbound messages. 
       """,

    'description': """
       This module extends the 'mail.notification' and 'mail.mail' models to modify the footer on outbound email messages.        
    	""",

    'author': "Brent Shreve",
    'website': "https://github.com/tsbrents",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
