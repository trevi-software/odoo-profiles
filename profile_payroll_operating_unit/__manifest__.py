# Copyright (C) 2019,2021 TREVI Software
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Payroll Operating Unit Profile",
    "summary": "Process payroll by operating units.",
    "version": "14.0.1.0.0",
    "author": "TREVI Software",
    "images": ["static/src/img/main_screenshot.png"],
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "AGPL-3",
    "category": "Payroll",
    "depends": [
        # https://github.com/OCA/operating-unit
        # https://github.com/trevi-software/trevi-hr
        "payroll_operating_unit",
        "payroll_operating_unit_access_all",
        "payroll_period_per_ou",
        "payroll_period_processing_per_ou",
    ],
    "data": [],
    "installable": True,
    "application": True,
}
