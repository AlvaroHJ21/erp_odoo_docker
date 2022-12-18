from odoo import models,fields

class Student(models.Model):
    _name  = 'student.add'

    name= fields.Char(string="student Name")
    age = fields.Integer()
