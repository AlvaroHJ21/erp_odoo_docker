from odoo import models, fields, api

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

# class Student(models.Model):
#     _name  = 'student.add'

#     name= fields.Char(string="Nombre")
#     age = fields.Integer(string="Edad")

#     genero = fields.Selection(
#         selection=GeneroFormat.SELECTION, 
#         default=GeneroFormat.MASCULINO,
#         string="Género"
#     )

class Career(models.Model):
    _name = 'career'
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

class Student(models.Model):
    _name = 'student.add'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string="Edad")
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    enrollment_date = fields.Date(string='Enrollment Date')
    # courses_ids = fields.Many2many('course', string='Courses')
    # grades_ids = fields.One2many('grade', 'student_id', string='Grades')
    major = fields.Many2one('career', string='Carrera')
    genero = fields.Selection(
        selection=GeneroFormat.SELECTION, 
        default=GeneroFormat.MASCULINO,
        string="Género"
    )

    # @api.depends('birth_date')
    # def _compute_age(self):
    #     for student in self:
    #         if student.birth_date:
    #             student.age = (fields.Date.today() - student.birth_date).years

