This will install the Payroll modules necessary to extend the base Odoo
system. Does not include HR.

Note (19.0): the operating-unit payroll dependencies
(``payroll_operating_unit``, ``payroll_operating_unit_access_all``,
``payroll_period_per_ou``, ``payroll_period_processing_per_ou``) have not
been migrated to 19.0 yet, so this profile is currently a placeholder that
installs nothing on its own. The modules are listed as comments in the
manifest and will be re-added when trevi-payroll migrates them.
