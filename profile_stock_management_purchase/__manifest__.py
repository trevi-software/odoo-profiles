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
    "name": "Stock Management + Purchasing Profile",
    "version": "14.0.1.0.0",
    "author": "TREVI Software",
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "AGPL-3",
    "images": ["static/src/img/main_screenshot.png"],
    "category": "Stock Management",
    "depends": [
        "profile_stock_management",
        # https://github.com/OCA/stock-logistics-warehouse
        "stock_mts_mto_rule",
        "stock_orderpoint_purchase_link",
        "stock_request_purchase",
    ],
    "data": [],
    "installable": True,
    "application": True,
}
