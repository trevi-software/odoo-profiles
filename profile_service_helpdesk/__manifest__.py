# Copyright (C) 2019 TREVI Software
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Help Desk and Service Profile",
    "version": "19.0.1.0.0",
    "author": "TREVI Software",
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "LGPL-3",
    "images": ["static/src/img/main_screenshot.png"],
    "category": "Helpdesk",
    "depends": [
        # https://github.com/trevi-software/trevi-misc
        # "project_portal_hide",  # not yet migrated to 19.0 upstream
        # "purchase_portal_hide",  # not yet migrated to 19.0 upstream
        # "sale_portal_hide",  # not yet migrated to 19.0 upstream
        # https://github.com/OCA//account-invoicing
        # "account_portal_hide_invoice",  # not yet migrated to 19.0 upstream
        # https://github.com/OCA/contract
        # "agreement",  # not yet migrated to 19.0 upstream
        # "agreement_legal",  # not yet migrated to 19.0 upstream
        # "agreement_sale",  # not yet migrated to 19.0 upstream
        # "agreement_serviceprofile",  # not yet migrated to 19.0 upstream
        "contract",
        "contract_payment_mode",
        "contract_sale",
        # https://github.com/OCA/field-service
        "fieldservice",
        "fieldservice_account",
        # "fieldservice_account_analytic",  # not yet migrated to 19.0 upstream
        "fieldservice_activity",
        # "fieldservice_agreement",  # depends on agreement: not yet migrated to 19.0 upstream
        "fieldservice_calendar",
        # "fieldservice_isp_account",  # not yet migrated to 19.0 upstream
        # "fieldservice_isp_flow",  # not yet migrated to 19.0 upstream
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
        # "project_task_dependency",  # not yet migrated to 19.0 upstream
        # "project_task_material",  # not yet migrated to 19.0 upstream
        # "project_template",  # not yet migrated to 19.0 upstream
        # https://github.com/OCA/website
        # "website_odoo_debranding",  # not yet migrated to 19.0 upstream
    ],
    "data": [],
    "installable": True,
    "application": True,
}
