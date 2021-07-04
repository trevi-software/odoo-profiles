# -*- coding: utf-8 -*-
#########################################################################
# Copyright (c) 2017-2019 TREVI Software Design and Computer Maintenance     #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#########################################################################

{
    "name": "Sale/CRM Profile",
    "summary": "Modules bundle for Sales & CRM",
    "description": """
Features
========
* Mostly usability enhancements in Sales and CRM
    """,
    "author": "TREVI Software Design and Computer Maintenance",
    "website": "http://",
    "version": "14.0.1.0.0",
    "category": "Sales Management",
    "license": "AGPL-3",
    "depends": [

	'crm',
        'l10n_et',
	'sale_management',

        # https://github.com/akretion/odoo-usability
        'product_usability',
        'sale_usability',

        # https://github.com/OCA/crm
        'crm_claim',
        'crm_lead_code',
        'crm_phonecall',
    ],
    "data": [
    ],
    "installable": True,
    "application": True,
}
