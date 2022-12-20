{
    'name': 'Sistema de Gestion de Estudiantes',
    'author': 'Grupo 5',
    'category':'Extra Tools',
    'version': '1.0.0',
    'license': 'AGPL-3',
    'summary': 'Gestion de estudiantes',
    'description': 'Gestion de estudiantes',
    'depends': ['base'],
    'data': [
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/course_view.xml',
        'views/matricula_view.xml',
        'views/group_view.xml',
        "views/menu.xml",
        'security/ir.model.access.csv'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto-install': False
}