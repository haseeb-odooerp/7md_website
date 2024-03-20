from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home  # Import the Home class

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