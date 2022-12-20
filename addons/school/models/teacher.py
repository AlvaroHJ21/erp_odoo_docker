from odoo import models, fields

class Teacher(models.Model):
    _name = 'teacher'
    name = fields.Char(string='Nombre', required=True)
    # subject_ids = fields.Many2many('school.subject', string='Materias')