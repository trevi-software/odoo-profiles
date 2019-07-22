# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   Copyright (C) 2019 Trevi Software (http://trevi.et).
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

{'name': 'Base Profile',
 'version': '12.0.1.0.0',
 'author': 'Akretion, Trevi Software',
 'website': 'http://trevi.et',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
    This will install the minimal modules necessary to extend the base module.
 """,
 'depends': [

     # https://github.com/akretion/odoo-usability
     'base_partner_ref',
     'base_usability',
     'eradicate_quick_create',
     'partner_tree_default',

     # https://github.com/OCA/server-brand
     'disable_odoo_online',

     # https://github.com/OCA/server-tools
     'auditlog',
     'scheduler_error_mailer',

     # https://github.com/OCA/server-ux
     'base_technical_features',

     # https://github.com/OCA/web
     'web_advanced_search',
     'web_dialog_size',
     'web_export_view',
     'web_responsive',
     'web_searchbar_full_width',
 ],
 'data': [
 ],
 'installable': True,
 'auto_install': True,
 'application': True,
 }
