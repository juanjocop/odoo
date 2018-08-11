# -*- coding: utf-8 -*-
from odoo import http

# class Ecoworld(http.Controller):
#     @http.route('/ecoworld/ecoworld/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ecoworld/ecoworld/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ecoworld.listing', {
#             'root': '/ecoworld/ecoworld',
#             'objects': http.request.env['ecoworld.ecoworld'].search([]),
#         })

#     @http.route('/ecoworld/ecoworld/objects/<model("ecoworld.ecoworld"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ecoworld.object', {
#             'object': obj
#         })