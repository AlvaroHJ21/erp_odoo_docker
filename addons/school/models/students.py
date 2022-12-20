from odoo import models,fields

class GeneroFormat:

    MASCULINO = "Masculino"
    FEMENINO = "Femenino"
    OTRO = "Otro"

    OPTIONS = [
        MASCULINO,
        FEMENINO,
        OTRO,

    ]
    SELECTION = [
        ("Masculino", MASCULINO),
        ("Femenino", FEMENINO),
        ("Otro", OTRO),
    ]

class Student(models.Model):
    _name  = 'student.add'

    name= fields.Char(string="student Name")
    age = fields.Integer()

    genero = fields.Selection(
        selection=GeneroFormat.SELECTION, 
        default=GeneroFormat.MASCULINO,
        string="Formato"
    )
