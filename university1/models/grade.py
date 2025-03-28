from odoo import models, fields

class Grade(models.Model):
    _name = 'university.grade'
    _description = 'Grade'

    student_id = fields.Many2one('university.student', string="Student")
    enrollment_id = fields.Many2one('university.enrollment', string="Enrollment")
    value = fields.Float(string="Grade")
