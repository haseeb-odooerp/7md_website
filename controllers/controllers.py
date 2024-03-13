# -*- coding: utf-8 -*-
import base64

from odoo.http import request
from odoo import http


class MdWebsite(http.Controller):
    @http.route('/', auth='public', type='http', website=True)
    def index(self, **kw):
        return request.render('7md_website.home')
    

class about7md(http.Controller):
    @http.route('/about', auth='public', type='http', website=True)
    def index(self, **kw):
        return request.render('7md_website.about')
    

class contact7md(http.Controller):
    @http.route('/contact', auth='public', type='http', website=True)
    def index(self, **kw):
        return request.render('7md_website.contact')
    

