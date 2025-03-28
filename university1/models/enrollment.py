from odoo import models, fields

class Enrollment(models.Model):
    _name = 'university.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('university.student', string="Student")
    university_id = fields.Many2one('university.university', string="University")
    teacher_id = fields.Many2one('university.teacher', string="Teacher")
    subject_id = fields.Many2one('university.subject', string="Subject")
    grade_ids = fields.One2many('university.grade', 'enrollment_id', string="Grades")
