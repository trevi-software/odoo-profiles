# Copyright (C) 2019 TREVI Software
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Help Desk and Service Profile',
    'version': '12.0.1.0.0',
    'author': 'Trevi Software',
    'website': 'http://trevi.et',
    'license': 'LGPL-3',
    'category': 'Helpdesk',
    'description': """
    This will install modules for a fully functional Helpdesk and field
    service management system.
""",
    'depends': [

     # https://github.com/OCA/contract
     'agreement',

     # https://github.com/OCA/field-service
     'fieldservice',
     'fieldservice_agreement',
     'fieldservice_delivery',
     'fieldservice_maintenance',
     'fieldservice_recurring',
     'fieldservice_repair',
     'fieldservice_stock',

     # https://github.com/OCA/project
     'project_template',

     # https://github.com/trevi-software/osi-addons/
     'agreement_helpdesk',
     'agreement_sale_subscription',
     'fieldservice_agreement_helpdesk',
     'fieldservice_helpdesk_stock',
     'helpdesk_fieldservice',
     'helpdesk_phone',
     'helpdesk_resolution',
     'helpdesk_stock',
     'helpdesk_ticket_to_task',
     'sale_subscription_suspend',

     # Enterprise
     'helpdesk',
     'helpdesk_sale_timesheet',
     'helpdesk_timesheet',
     'website_form_editor',
     'website_enterprise',
     'website_helpdesk',
     'website_helpdesk_form',
     'website_helpdesk_slides',

     # https://github.com/Openworx/odoo-addons
     'login_page',
    ],
    'data': [
    ],
    'installable': True,
    'application': True,
 }
