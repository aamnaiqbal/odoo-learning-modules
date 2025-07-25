{
    'name': 'Patient Appointment System',
    'version': '1.0',
    'depends': ['base'],
    'category': 'Healthcare',
    'author': 'Aamna Iqbal',
    'description': 'Manage patient appointments',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
    ],
    'installable': True,
    'application': True,
}
