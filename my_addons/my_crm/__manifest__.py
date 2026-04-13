{
    'name': '客户订单管理',
    'version': '1.0',
    'category': 'CRM',
    'summary': '客户订单管理模块',
    'description': """
    客户订单管理
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # 新增：权限文件
        'security/record_rule.xml',
        'data/sequence.xml',
        'views/crm_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}