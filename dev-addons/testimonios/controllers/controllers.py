# -*- coding: utf-8 -*-
from odoo import http

class Testimonios(http.Controller):

    @http.route('/testimonios', auth='public', website=True)
    def testimonios(self, **kw):
        Testimonios = http.request.env['guiaeco.testimonios']
        return http.request.render('testimonios.ecoworld_testimonios',
        {'testimonios': Testimonios.search([('activo', '=', True)], limit=100, order="create_date desc")})
