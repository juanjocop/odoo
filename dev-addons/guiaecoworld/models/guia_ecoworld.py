# -*- coding: utf-8 -*-

from odoo import models, fields, api

class guiaecoworld(models.Model):
    _name = 'guiaeco.clientes'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner')
    activo = fields.Boolean()
    especialidad = fields.Char()
    mapaG = fields.Char()
    calidadPresentacion = fields.Char()
    calidadTrato = fields.Char()
    calidadRecomienda = fields.Boolean()
    calidadBeneficios = fields.Char()
    calidadValora = fields.Integer()
    imagenPlaca = fields.Binary()
    cabecera = fields.Binary()
    enlaceWeb = fields.Char()
    enlaceFacebook = fields.Char()
    descripcion = fields.Text()
