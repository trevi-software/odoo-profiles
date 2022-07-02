###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2019,2021,2022 Trevi Software (http://trevi.et).
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
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

{
    "name": "Base Profile",
    "version": "14.0.1.0.0",
    "author": "Akretion, TREVI Software",
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "images": ["static/src/img/main_screenshot.png"],
    "depends": [
        # https://github.com/akretion/odoo-usability
        "base_usability",
        "base_partner_one2many_phone",
        "partner_tree_default_base",
        "partner_tree_default_contacts",
        # https://github.com/OCA/partner-contact
        "partner_address_version",
        "partner_vat_unique",
        # https://github.com/OCA/server-backend
        "base_user_role",
        # https://github.com/OCA/server-brand
        "disable_odoo_online",
        "remove_odoo_enterprise",
        # https://github.com/OCA/server-tools
        "auditlog",
        "mail_debrand",
        # https://github.com/OCA/server-ux
        "base_technical_features",
        # https://github.com/OCA/web
        "web_advanced_search",
        "web_dialog_size",
        "web_drop_target",
        "web_group_expand",
        "web_listview_range_select",
        "web_no_bubble",
        "web_refresher",
        "web_responsive",
        # https://github.com/OCA/social
        "mail_tracking",
    ],
    "data": [],
    "installable": True,
    "auto_install": True,
    "application": True,
}
