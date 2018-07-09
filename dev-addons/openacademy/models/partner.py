# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean("Instructor", default=False)

    sesion_id = fields.Many2many("openacademy.sesion", string="Sesion Atendida", readonly=True)
