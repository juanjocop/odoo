# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class guiaeco(models.Model):
#     _name = 'guiaeco.guiaeco'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class guiaecoworld(models.Model):
    _name = 'guiaeco.clientes'

    id_cliente = fields.Many2one("res.partner", string="Cliente")
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
