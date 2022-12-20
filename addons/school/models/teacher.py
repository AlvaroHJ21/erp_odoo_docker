from odoo import models, fields

class Teacher(models.Model):
    _name = 'teacher'
    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Telefono', required=True)
    # subject_ids = fields.Many2many('school.subject', string='Materias')