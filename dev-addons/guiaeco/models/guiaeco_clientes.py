# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class dev-addons/library(models.Model):
#     _name = 'dev-addons/library.dev-addons/library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class GuiaecoClientes(models.Model):
    _name = 'guiaeco.clientes'

    idcliente = fields.Integer(string='Id Cliente')
    activo = fields.Boolean(string='Activo?')
    especialidad = fields.Char(string='Especialidad')
    mapaG = fields.Char(string='Enlace Mapa')
    calidadPresentacion = fields.Char(string='Como valora la presentación del producto?')
    calidadTrato = fields.Char(string='Trato recibido por parte de los agentes')
    calidadRecomienda = fields.Boolean(string='Lo recomendaría a otras personas?')
    calidadBeneficios = fields.Char(string='Beneficios importantes para usted y su negocio')
    calidadValora = fields.Integer(string='Como valora eOZONE y ecoWORLD?')
    imagenPlaca = fields.Binary(string='Imagen placa cliente')
    cabecera = fields.Binary(string='Cabecera cliente')
