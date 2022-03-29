# Copyright (C) 2019,2021 TREVI Software
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{'name': 'HRM Profile',
 'summary': 'Complete Human Resources application',
 'version': '14.0.1.0.0',
 'author': 'Trevi Software',
 'website': 'http://trevi.et',
 'license': 'AGPL-3',
 'category': 'Human Resources',
 'depends': [

     # https://github.com/OCA/hr
     # https://github.com/trevi-software/trevi-hr
     "hr_accrual_bank",
     "hr_benefit",
     "hr_contract_reference",
     "hr_contract_status",
     "hr_contract_values_resource_schedule",
     "hr_employee_id",
     "hr_employee_medical_examination",
     "hr_employee_relative",
     "hr_employee_seniority_months",
     "hr_employee_status",
     "hr_job_change_state",
     "hr_jobs_hierarchy",
     "hr_job_transfer",
     "hr_leave_type_unique",
     "hr_photobooth",
     "trevi_hr_job_categories",
     "trevi_hr_public_holidays",
     "trevi_hr_usability",
 ],
 'data': [
 ],
 'installable': True,
 'auto_install': True,
 'application': True,
 }
