# -*- coding: utf-8 -*-
from odoo import http

# class Guiaeco(http.Controller):
#     @http.route('/guiaeco/guiaeco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/guiaeco/guiaeco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('guiaeco.listing', {
#             'root': '/guiaeco/guiaeco',
#             'objects': http.request.env['guiaeco.guiaeco'].search([]),
#         })

#     @http.route('/guiaeco/guiaeco/objects/<model("guiaeco.guiaeco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('guiaeco.object', {
#             'object': obj
#         })