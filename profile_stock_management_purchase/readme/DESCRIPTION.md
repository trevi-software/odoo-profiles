This application will install modules for a fully functional stock
management and Purchasing system.

Note (19.0): the purchasing-specific dependencies (``stock_mts_mto_rule``,
``stock_orderpoint_purchase_link``, ``stock_request_purchase``) have not
been migrated to 19.0 upstream yet, so this profile currently installs
only the stock-management set from ``profile_stock_management``. The
purchasing modules are listed as comments in the manifest and will be
re-added when OCA/stock-logistics-warehouse migrates them.
