# -*- coding: utf-8 -*-
from odoo import http

# class Dev-addons/library(http.Controller):
#     @http.route('/dev-addons/library/dev-addons/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev-addons/library/dev-addons/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev-addons/library.listing', {
#             'root': '/dev-addons/library/dev-addons/library',
#             'objects': http.request.env['dev-addons/library.dev-addons/library'].search([]),
#         })

#     @http.route('/dev-addons/library/dev-addons/library/objects/<model("dev-addons/library.dev-addons/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev-addons/library.object', {
#             'object': obj
#         })