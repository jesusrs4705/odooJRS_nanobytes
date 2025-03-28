from odoo import models, fields

class Subject(models.Model):
    _name = 'university.subject'
    _description = 'Subject'

    name = fields.Char(string="Name", required=True)
    university_id = fields.Many2one('university.university', string="University")
    teacher_ids = fields.Many2many('university.teacher', string="Teachers")
    enrollment_ids = fields.One2many('university.enrollment', 'subject_id', string="Enrollments")
