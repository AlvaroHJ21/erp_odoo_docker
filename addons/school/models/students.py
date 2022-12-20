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

# class Student(models.Model):
#     _name  = 'student.add'

#     name= fields.Char(string="Nombre")
#     age = fields.Integer(string="Edad")

#     genero = fields.Selection(
#         selection=GeneroFormat.SELECTION, 
#         default=GeneroFormat.MASCULINO,
#         string="Género"
#     )

class Student(models.Model):
    _name = 'student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    enrollment_date = fields.Date(string='Enrollment Date')
    # courses_ids = fields.Many2many('course', string='Courses')
    # grades_ids = fields.One2many('grade', 'student_id', string='Grades')
    genero = fields.Selection(
        selection=GeneroFormat.SELECTION, 
        default=GeneroFormat.MASCULINO,
        string="Género"
    )

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                student.age = (fields.Date.today() - student.birth_date).years
