{
    'name': 'University',
    'version': '1.0',
    'summary': 'University management module',
    'author': 'Jesus Rodriguez',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/university_views.xml',
        'views/department_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml',
        'views/student_views.xml',
        'views/enrollment_views.xml',
        'views/grade_views.xml',
        'views/university_report_views.xml',
        'views/menu.xml',
    ],
    'application': True,
}
