{
    'name': 'Login/signup reCAPTCHA',
    'version': '16.0.1.0.0',
    'summary': """Protect robot login and signup with reCAPTCHA""",
    'author': 'Oakland Odoo ERP',
    'company': 'Oakland Odoo ERP',
    'website': 'https://www.odooerp.ae',
    'category': 'Extra Tools',
    'depends': ['base'],
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'depends': ['base', 'web', '7md_website'],
    'data': [
        'static/templates/header.xml',
        'views/captcha_views.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            "oe_login_signup/static/src/js/captcha.js",
            "oe_login_signup/static/src/js/autofill.js",
            ],
    },
    'installable': True,
    'auto_install': False,

}
