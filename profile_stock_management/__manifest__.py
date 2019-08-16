# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2018 TREVI Software Design and Computer Maintenance.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Stock Management Profile',
    'version': '12.0.1.0.0',
    'author': 'Trevi Software',
    'website': 'http://trevi.et',
    'license': 'AGPL-3',
    'category': 'Generic Modules',
    'description': """
    This will install modules for a fully functional stock management system.
""",
    'depends': [

     'l10n_et',

     # https://github.com/OCA/product-attribute
     'product_code_unique',

     # https://github.com/OCA/stock-logistics-reporting
     'stock_report_quantity_by_location',

     # https://github.com/OCA/stock-logistics-warehouse
     'stock_demand_estimate',
     'stock_inventory_chatter',
     'stock_inventory_discrepancy',
     'stock_inventory_lockdown',
     'stock_inventory_verification_request',
     'stock_orderpoint_move_link',
     'stock_packaging',
     'stock_request',
     'stock_request_tier_validation',

     # https://github.com/OCA/stock-logistics-workflow
     'stock_no_negative',
     'stock_picking_show_backorder',
    ],
    'data': [
    ],
    'installable': True,
    'application': True,
 }
