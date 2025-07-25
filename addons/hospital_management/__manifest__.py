{
    'name': 'Hospital Management', #required field
    'version': '1.0.0', #required field
    'category': 'Healthcare',
    'summary': 'Hospital Management System',
    'description': 'A basic hospital management module',
    'author': 'Aamna Iqbal',
    'depends': ['base'], #required field.    The depends field lists the Odoo modules that your module depends on. These must be installed for your module to work correctly.
    'license': 'LGPL-3',
    'data': [],   #required field.  The data field is a list of XML/CSV files that should be loaded when the module is installed.
    'installable': True,
    'application': True,
}