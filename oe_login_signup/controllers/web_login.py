from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home  # Import the Home class
import importlib
contact7md = importlib.import_module("odoo.addons.7md_website.controllers.controllers").contact7md

class AuthRemember(Home):  # Inherit from Home instead of http.Controller

    @http.route()  # Use the same route as the original web_login
    def web_login(self, redirect=None, **kw):
        response = super(AuthRemember, self).web_login(redirect, **kw)  # Now super() correctly refers to Home
        if request.params.get('login_success'):
            if 'remember_me' in request.params:  # Make sure this matches your checkbox's name attribute
                # Generate and store token logic goes here
                # Remember to set the cookie in the response
                user = request.env['res.users'].sudo().search([('login', '=', request.params['login'])])
                if user:
                    token = "GENERATED_SECURE_TOKEN"  # Replace with actual token generation logic
                    response.set_cookie('remember_token', token, max_age=30*24*60*60)  # Example: 30 days expiry
        return response


class ExtendedContact7md(contact7md):
    @http.route([
        '/contact',
        '/contact/<string:store_name>',
        ], auth='public', type='http', website=True)
    def index(self, store_name=None, **kw):
        values = {
            'stores': request.env['oe.store.location'].sudo().search([]),
            'store_url': store_name if store_name else False
        }
        return request.render('7md_website.contact', values)

class ContactFormController(http.Controller):
    @http.route([
        '/contact/submit',
        '/contact/<string:store_name>/submit',
        ], type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def contact_submit(self, store_name=None, **post):
        # You can do some data validation here if necessary

        # Create lead in CRM
        request.env['crm.lead'].sudo().create({
            'name': post.get('name'),
            'contact_name': post.get('name'),
            'email_from': post.get('email'),
            'phone': post.get('phone'),
            'description': post.get('message'),
        })

        # Redirect to a 'Thank You' page or back to the contact page with a success message
        return request.render('your_module.thank_you_template', {})