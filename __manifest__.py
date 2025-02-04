# __manifest__.py
{
    'name': 'Evaluación de Desempeño',
    'version': '16.0.1.0.0',
    'summary': 'Gestión de Evaluaciones de Desempeño para Empleados',
    'category': 'Human Resources',
    'author': 'Adrián Bejarano Mora',
    'license': 'AGPL-3',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/evaluacion_desempeno_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}