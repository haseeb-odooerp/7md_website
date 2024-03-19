# -*- coding: utf-8 -*-
import base64

from odoo.http import request
from odoo import http


class MdWebsite(http.Controller):
    @http.route('/', auth='public', type='http', website=True)
    def index(self, **kw):
        category = kw.get('category')
        search = kw.get('search')
        if category and not search:
            return request.render('7md_website.home')
        if category and search:
            return request.redirect('/shop?category=%s&search=%s' % (category, search))
        if search and not category:
            return request.redirect('/shop?search=%s' % search)
        return request.render('7md_website.home')


class about7md(http.Controller):
    @http.route('/about', auth='public', type='http', website=True)
    def index(self, **kw):
        return request.render('7md_website.about')
    

class contact7md(http.Controller):
    @http.route('/contact', auth='public', type='http', website=True)
    def index(self, **kw):
        return request.render('7md_website.contact')
    

class websitePolicies(http.Controller):

    @http.route('/privacy_policy', auth='public', type='http', website=True)
    def privacyPolicy7md(self, **kw):

        return request.render('privacy_policy_7md')

    @http.route('/return_policy', auth='public', type='http', website=True)
    def returnPolicy(self, **kw):

        return request.render('return_policy_7md')


    @http.route('/terms_and_conditions', auth='public', type='http', website=True)
    def termAndCondition(self, **kw):
        
        return request.render('terms_and_condition_7md')
    
