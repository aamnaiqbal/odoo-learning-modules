{
    'name': 'Hospital Website',
    'version': '1.0',
    'category': 'Website',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_menu.xml',
        'views/appointment_backend_views.xml',
        'views/homepage_template.xml',
        'views/departments_template.xml',
        'views/doctors_template.xml',
        'views/appointment_template.xml',
        'data/demo_departments.xml',
        'data/demo_doctors.xml',
    ],
    'demo': [
        'data/demo_departments.xml',
        'data/demo_doctors.xml',
    ],
    'installable': True,
    'application': True,
}
