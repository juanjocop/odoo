# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class contactoeco(models.Model):
    _inherit = 'res.partner'

    enlaceFacebook = fields.Char(string="Facebook Link")
    referido = fields.Many2one('res.partner', string="Referido por")
    referidos = fields.One2many('res.partner', 'referido', string="Referidos")
    cifnif = fields.Char(string="NIF/CIF")
    nombrefiscal = fields.Char(string="Nombre Fiscal")

    @api.constrains('cifnif')
    @api.one
    def _checka_cifnif(self):
        if self.cifnif:
            if len(self.cifnif)>9:
                raise ValidationError('El CIF/NIF no puede exceder los 9 caracteres')
