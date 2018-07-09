# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.curso'

    name = fields.Char(string="Título", required=True)
#    value = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string="Descripción")

    responsable_id =fields.Many2one("res.users", ondelete="set null", string="Responsable", index=True)
    sesion_id = fields.One2many("openacademy.sesion", "curso_id", string="Sesiones")
#
#    @api.depends('value')
#    def _value_pc(self):
#        self.value2 = float(self.value) / 100

class Sesion(models.Model):
    _name = 'openacademy.sesion'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duración en días")
    seats = fields.Integer(string="Número de asientos")

    instructor_id = fields.Many2one("res.partner", string="Instructor")
    curso_id = fields.Many2one("openacademy.curso", ondelete="cascade", string="Curso", required=True)
    asistente_id = fields.Many2many("res.partner", string="Asistente")
