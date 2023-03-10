{
    'name': 'Approval Block',
    'sequence': 1,
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/approval_block.xml',
        'views/approval_block_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}
