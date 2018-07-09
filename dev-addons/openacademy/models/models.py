# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Course(models.Model):
    _name = 'openacademy.curso'

    name = fields.Char(string="Título", required=True)
#    value = fields.Integer()
#    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string="Descripción")

    responsable_id =fields.Many2one("res.users", ondelete="set null", string="Responsable", index=True)
    sesion_id = fields.One2many("openacademy.sesion", "curso_id", string="Sesiones")

    # debido al sql constrint ya no se pueden duplicar cursos, hay que definir la copia para que no se pise la clave

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count([('name', '=like', u"Copia of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copia of {}".format(self.name)
        else:
            new_name = u"Copia of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ("name_description_check",
        "CHECK(name != description)",
        "El título del curso no debe estar en la descripción"),

        ('name_unique',
        'UNIQUE(name)',
        "El curso debe ser único no puede estar repetido"),
    ]

class Sesion(models.Model):
    _name = 'openacademy.sesion'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duración en días")
    seats = fields.Integer(string="Número de asientos")
    activo = fields.Boolean(default=True)

    instructor_id = fields.Many2one("res.partner", string="Instructor", domain=["|", ("instructor", "=", True), ("category_id.name", "ilike", "Teacher")])
    curso_id = fields.Many2one("openacademy.curso", ondelete="cascade", string="Curso", required=True)
    asistente_id = fields.Many2many("res.partner", string="Asistente")

    asientos_ocupados = fields.Float(string="Asientos ocupados", compute="_asientos_ocupados")

    @api.depends("seats", "asistente_id")
    def _asientos_ocupados(self):
        for r in self:
            if not r.seats:
                r.asientos_ocupados = 0.0
            else:
                r.asientos_ocupados = 100.0 * len(r.asistente_id) / r.seats

    @api.onchange("seats", "asistente_id")
    def _verifica_asientos_validos(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Valor de 'asiento' incorrecto",
                    'message': "El número de asientos disponibles no puede ser menor a 0",
                },
            }
        if self.seats < len(self.asistente_id):
            return {
                'warning': {
                    'title': "Demasiados asistentes",
                    'message': "Incrementa el número de asientos o reduce el número de asistentes",
                },
            }

    @api.constrains("instructor_id", "asistente_id")
    def _check_instructor_not_in_asistente(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.asistente_id:
                raise exceptions.ValidationError("El instructor de la sesión no puede ser un asistente")
