# Copyright (C) 2019 TREVI Software
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Help Desk and Service Profile',
    'version': '14.0.1.0.0',
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
     'agreement_legal',
     'agreement_sale',
     'agreement_serviceprofile',
     'contract',
     'contract_payment_mode',
     'contract_sale',

     # https://github.com/OCA/field-service
     'fieldservice',
     'fieldservice_account',
     'fieldservice_account_analytic',
     'fieldservice_activity',
     'fieldservice_agreement',
     'fieldservice_isp_flow',
     'fieldservice_project',
     'fieldservice_purchase',
     'fieldservice_recurring',
     'fieldservice_sale',
     'fieldservice_skill',
     'fieldservice_stage_server_action',
     'fieldservice_stage_validation',
     'fieldservice_timeline',

     # https://github.com/OCA/helpdesk
     'helpdesk_mgmt',
     'helpdesk_mgmt_project',
     'helpdesk_type',

     # https://github.com/OCA/project
     'project_task_dependency',
     'project_task_material',
     'project_template',

     # https://github.com/OCA/website
     'website_odoo_debranding',

     # https://github.com/trevi-software/osi-addons/
     #'agreement_helpdesk',
     #'agreement_sale_subscription',
     #'fieldservice_agreement_helpdesk',
     #'fieldservice_helpdesk_stock',
     #'helpdesk_fieldservice',
     #'helpdesk_phone',
     #'helpdesk_resolution',
     #'helpdesk_stock',
     #'helpdesk_ticket_to_task',
     #'sale_subscription_suspend',
    ],
    'data': [
    ],
    'installable': True,
    'application': True,
 }
