# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   Copyright (C) 2019,2021 Trevi Software (http://trevi.et).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{'name': 'HRM Profile',
 'version': '14.0.1.0.0',
 'author': 'Akretion, Trevi Software',
 'website': 'http://trevi.et',
 'license': 'AGPL-3',
 'category': 'Human Resources',
 'description': """
    This will install the HR modules necessary to extend the base module.
    Does not include Payroll.
 """,
 'depends': [

     # https://github.com/OCA/hr
     "hr_contract_reference",
     "hr_employee_id",
     "hr_employee_medical_examination",
     "hr_employee_relative",
 ],
 'data': [
 ],
 'installable': True,
 'auto_install': True,
 'application': True,
 }
