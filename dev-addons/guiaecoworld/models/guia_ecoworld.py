# -*- coding: utf-8 -*-

from odoo import models, fields, api

class guiaecoworld(models.Model):
    _name = 'guiaeco.clientes'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', domain=[('is_company', '=', True)])
    activo = fields.Boolean()
    especialidad = fields.Char()
    mapaG = fields.Char()
    calidadPresentacion = fields.Char(string="Presentación")
    calidadTrato = fields.Char(string="Trato recibido")
    calidadRecomienda = fields.Boolean(string="Nos Recomienda?")
    calidadBeneficios = fields.Char(string="Beneficios")
    calidadValora = fields.Integer(string="Valoración General")
    imagenPlaca = fields.Binary(string="Foto con Placa")
    cabecera = fields.Binary(string="Imagen de cabecera")
    enlaceFacebook = fields.Char(string="Facebook Link")
    descripcion = fields.Text(string="Testimonio")

class contactoeco(models.Model):
    _inherit = 'res.partner'

    enlaceFacebook = fields.Char()
