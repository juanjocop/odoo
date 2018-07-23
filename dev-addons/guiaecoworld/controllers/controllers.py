# -*- coding: utf-8 -*-
from odoo import http

class Guiaeco(http.Controller):
    @http.route('/guiaecoworld', auth='public', website=True)
    def guiaeco(self, **kw):
        Clientes = http.request.env['guiaeco.clientes']
        return http.request.render('guiaecoworld.guiaecoworld_contenido',
            {'clientes4': Clientes.search([('activo', '=', True)], limit=4, order="fechaIncorporacion desc"),
            'clientes': Clientes.search([('activo', '=', True)], limit=100, order="name")})

    @http.route('/guiaecoworld/<int:lugar>', auth='public', website=True)
    def guiaecoprovincia(self, lugar, search, type, **kw):
        if type == 'provincia':
            Clientes = http.request.env['guiaeco.clientes']
            return http.request.render('guiaecoworld.guiaecoworld_contenido',
                {'clientes4': Clientes.search([('activo', '=', True), ('state_id', '=', lugar)], limit=4, order="fechaIncorporacion desc"),
                'provincia': search,
                'clientes': Clientes.search([('activo', '=', True), ('state_id', '=', lugar)], limit=100, order="name")})
        elif type == 'localidad':
            Clientes = http.request.env['guiaeco.clientes']
            return http.request.render('guiaecoworld.guiaecoworld_contenido',
                {'clientes4': Clientes.search([('activo', '=', True), ('city', '=', search)], limit=4, order="fechaIncorporacion desc"),
                'localidad': search,
                'clientes': Clientes.search([('activo', '=', True), ('city', '=', search)], limit=100, order="name")})

#    @http.route('/guiaecoworld/localidad/<int:localidad>', auth='public', website=True)
#    def guiaecolocalidad(self, localidad, search, type, **kw):
#        Clientes = http.request.env['guiaeco.clientes']
#        return http.request.render('guiaecoworld.guiaecoworld_contenido',
#        {'clientes4': Clientes.search([('activo', '=', True), ('city', '=', search)], limit=4, order="fechaIncorporacion desc"),
#        'localidad': search})

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
