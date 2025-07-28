{
    'name': 'Hospital Management', #required field. Module name
    'version': '1.0.0', #required field. Module version
    'category': 'Healthcare', #The category field is used to classify your module in the Odoo app store.
    'summary': 'Hospital Management System',
    'description': 'A basic hospital management module',
    'author': 'Aamna Iqbal',
    'depends': ['base'], #required field.    The depends field lists the Odoo modules that your module depends on. These must be installed for your module to work correctly.
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/patient_readonly_views.xml',
        'views/doctor_views.xml',
        'views/menu.xml'
    ],   #required field.  The data field is a list of XML/CSV files that should be loaded when the module is installed.
    'installable': True,
    'application': True,
}