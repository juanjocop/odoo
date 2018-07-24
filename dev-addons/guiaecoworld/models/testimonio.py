# -*- coding: utf-8 -*-

from odoo import models, fields, api

class testimonio(models.Model):
    _name = 'guiaeco.testimonios'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', domain=[('is_company', '=', False)], required=True, ondelete="restrict")
    activo = fields.Boolean(string="Testimonio Activado")
    testimonio = fields.Text(string="Testimonio")
    calidadPresentacion = fields.Selection([(1,'Bien'), (2,'Muy Bien'), (3,'Excelente')],string="Presentación")
    calidadTrato = fields.Selection([(1,'Correcto'), (2,'Agradable'), (3,'Excepcional')],string="Trato recibido")
    calidadRecomienda = fields.Boolean(string="Nos Recomienda?")
    calidadBeneficios = fields.Char(string="Beneficios")
    calidadValora = fields.Integer(string="Valoración General")
