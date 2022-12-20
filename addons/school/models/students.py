from odoo import models, fields, api
import datetime

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

# ---------------Curso------------------

class Course(models.Model):
    _name="course"
    name=fields.Char(string='Name', required=True)
    description = fields.Text(string="Description")
    crediting=fields.Integer(string='Creditos')

# ---------------Carrera------------------

class Career(models.Model):
    _name = 'career'
    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')

# ---------------Estudiante------------------

class Student(models.Model):
    _name = 'student.add'
    _description = 'Student Information'

    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad', compute='_compute_age')
    birth_date = fields.Date(string='Fecha de nacimiento')
    address = fields.Char(string='Dirección')
    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    enrollment_date = fields.Date(string='Enrollment Date')
    # courses_ids = fields.Many2many('course', string='Courses')
    # grades_ids = fields.One2many('grade', 'student_id', string='Grades')
    major = fields.Many2one('career', string='Carrera')
    # course = fields.Many2many('course', string='Cursos')

    genero = fields.Selection(
        selection=GeneroFormat.SELECTION, 
        default=GeneroFormat.MASCULINO,
        string="Género"
    )

    @api.depends('birth_date')
    def _compute_age(self):
        today = datetime.date.today()
        for record in self:
            if record.birth_date:
                age = today.year - record.birth_date.year
                if today.month < record.birth_date.month or (today.month == record.birth_date.month and today.day < record.birth_date.day):
                    age -= 1
                record.age = age

# ---------------PROFESOR------------------

class Teacher(models.Model):
    _name = 'teacher'
    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Teléfono', required=True)
    # subject_ids = fields.Many2many('school.subject', string='Materias')

# ---------------GRUPO------------------

class Grupo(models.Model):
    _name = 'group'
    _description = 'Grupo de Estudiantes'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Descripción')
    course_id = fields.Many2one('course', string='Curso')
    teacher_id = fields.Many2one('teacher', string='Profesor')

# ---------------MATRICULA------------------

class Matricula(models.Model):
    _name = 'matricula'
    _description = 'Matricula de Estudiantes'
    
    semestre = fields.Selection(
        selection=[
            ("1", "2021-1"),
            ("2", "2021-2"),
            ("3", "2022-1"),
            ("4", "2022-2"),
            ("5", "2023-1"),
            ("6", "2023-2"),
        ],
        default="1",
        string="Semestre"
    )
    student_id = fields.Many2one('student.add', string='Estudiante')
    grupo_id = fields.Many2many('group', string='Grupo')

