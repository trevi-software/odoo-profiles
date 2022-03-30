# Copyright (C) 2019,2021 TREVI Software
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Payroll Profile",
    "summary": "Complete payroll application",
    "version": "14.0.1.0.0",
    "author": "TREVI Software",
    "images": ["static/src/img/main_screenshot.png"],
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "AGPL-3",
    "category": "Payroll",
    "depends": [
        # https://github.com/OCA/payroll
        # https://github.com/trevi-software/trevi-hr
        "hr_benefit_payroll",
        "hr_contract_values_payroll",
        "hr_employee_status_payroll",
        "payroll_payslip_amendment_contract_status",
        "payroll_period_account",
        "payroll_period_base_lock",
        "payroll_period_contract_values",
        "payroll_period_payslip_amendment",
        "payroll_period_processing",
        "payroll_policy_absence",
        "payroll_policy_accrual",
        "payroll_policy_ot",
        "payroll_policy_presence",
        "payroll_register",
    ],
    "data": [],
    "installable": True,
    "auto_install": True,
    "application": True,
}
