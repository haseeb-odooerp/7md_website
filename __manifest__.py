# -*- coding: utf-8 -*-
{
    'name': "7md_website",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        this module is for 7md ecommerce store
    """,

    'author': "OAKLAND - odooERP.ae",
    'website': "http://www.odooerp.ae",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates/header.xml',
        'templates/index.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend':[
            "7md_website/static/src/css/account.css",
            "7md_website/static/src/css/all.css",
            "7md_website/static/src/css/bootstrap-grid.css",
            "7md_website/static/src/css/bootstrap-grid.rtl.css",
            "7md_website/static/src/css/bootstrap-reboot.css",
            "7md_website/static/src/css/bootstrap-reboot.rtl.css",
            "7md_website/static/src/css/bootstrap-utilities.css",
            "7md_website/static/src/css/bootstrap-utilities.rtl.css",
            "7md_website/static/src/css/bootstrap.css",
            "7md_website/static/src/css/bootstrap.rtl.css",
            "7md_website/static/src/css/layout-767.css",
            "7md_website/static/src/css/layout-992.css",
            # "7md_website/static/src/css/layout-ar.css",
            "7md_website/static/src/css/layout.css",
            "7md_website/static/src/css/main-page.css",
            "7md_website/static/src/css/product-details.css",
            "7md_website/static/src/css/shopping-cart.css",
            "7md_website/static/src/css/updated-styles.scss",
            # "7md_website/static/src/js/bootstrap.bundle.min.js",
            # "7md_website/static/src/js/bootstrap.bundle.min.js.map",
        ],
    },
}
