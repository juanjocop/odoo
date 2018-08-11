# -*- coding: utf-8 -*-
{
    'name': "ecoworld",

    'summary': """
        Personalización odoo para ecoWORLD""",

    'description': """
        Con este modulo adaptamos odoo a las necesidades de ecoWORLD
    """,

    'author': "ecoWORLD",
    'website': "http://www.eco-world.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ecoWORLD',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Añadimos para que aparezca en aplicaicones a la primera
    'application': True,
}
