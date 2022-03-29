# Copyright (C) 2019 TREVI Software
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Help Desk and Service Profile",
    "version": "14.0.1.0.0",
    "author": "TREVI Software",
    "website": "https://github.com/OCA/odoo-profiles",
    "license": "LGPL-3",
    "images": ["static/src/img/main_screenshot.png"],
    "category": "Helpdesk",
    "depends": [
        # https://github.com/trevi-software/trevi-misc
        "project_portal_hide",
        "purchase_portal_hide",
        "sale_portal_hide",
        # https://github.com/OCA//account-invoicing
        "account_portal_hide_invoice",
        # https://github.com/OCA/contract
        "agreement",
        "agreement_legal",
        "agreement_sale",
        "agreement_serviceprofile",
        "contract",
        "contract_payment_mode",
        "contract_sale",
        # https://github.com/OCA/field-service
        "fieldservice",
        "fieldservice_account",
        "fieldservice_account_analytic",
        "fieldservice_activity",
        "fieldservice_agreement",
        "fieldservice_isp_flow",
        "fieldservice_project",
        "fieldservice_purchase",
        "fieldservice_recurring",
        "fieldservice_sale",
        "fieldservice_skill",
        "fieldservice_stage_server_action",
        "fieldservice_stage_validation",
        "fieldservice_timeline",
        # https://github.com/OCA/helpdesk
        "helpdesk_mgmt",
        "helpdesk_mgmt_project",
        "helpdesk_type",
        # https://github.com/OCA/project
        "project_task_dependency",
        "project_task_material",
        "project_template",
        # https://github.com/OCA/website
        "website_odoo_debranding",
    ],
    "data": [],
    "installable": True,
    "application": True,
}
