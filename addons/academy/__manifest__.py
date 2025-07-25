# academy/__manifest__.py
{
    'name': 'Academy',
    'version': '1.0',
    'category': 'Education',
    'depends': ['base'],
    'author': 'Your Name',
    'summary': 'Simple course management module',
    'description': 'A basic module to manage academy courses.',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/academy_course_views.xml',
    ],
    'installable': True,
    'application': True,
}
