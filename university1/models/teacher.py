from odoo import models, fields

class Teacher(models.Model):
    _name = 'university.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Name", required=True)
    university_id = fields.Many2one('university.university', string="University")
    department_id = fields.Many2one('university.department', string="Department")
    subject_ids = fields.Many2many('university.subject', string="Subjects")
    enrollment_ids = fields.One2many('university.enrollment', 'teacher_id', string="Enrollments")
