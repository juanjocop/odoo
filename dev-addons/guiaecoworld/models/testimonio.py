# -*- coding: utf-8 -*-

from odoo import models, fields, api

class testimonio(models.Model):
    _name = 'testimonios'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', domain=[('is_company', '=', False)])
    testimonio = fields.Char(string="Testimonio")
