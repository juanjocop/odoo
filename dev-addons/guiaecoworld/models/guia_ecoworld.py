# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class guiaecoworld(models.Model):
    _name = 'guiaeco.clientes'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', domain=[('is_company', '=', True)], required=True, ondelete="restrict")
    activo = fields.Boolean(string="Activado en Guía?")
    especialidad = fields.Char(string="Especialidad")
    mapaG = fields.Char(string="Mapa Google")
    mapaEmbed = fields.Char(string="Mapa Embed", help="Añadir solo codigo embed, despues de 'pb='")
    imagenPlaca = fields.Binary(string="Foto con Placa")
    cabecera = fields.Binary(string="Imagen de cabecera")
    fechaIncorporacion = fields.Date(string="Fecha Incorporación a Guía", required=True)
