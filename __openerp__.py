# -*- coding: utf-8 -*-
{
    'name': "account_payment_report",

    'summary': """
        Odoo custom report for account payments. 
        """,

    'description': """
        Odoo custom report for account payments. 
        By default there's no direct report print available in accounting -- > Sales -- > payments
        So this module will add a report button to print account payment reports. 
    """,

    'author': "Tradetec",
    'website': "http://www.tradetec.info",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ]
}