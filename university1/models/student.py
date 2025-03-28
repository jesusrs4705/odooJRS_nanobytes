from odoo import models, fields

class Student(models.Model):
    _name = 'university.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    university_id = fields.Many2one('university.university', string="University")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Postal Code")
    state_id = fields.Many2one('res.country.state', string="State")
    country_id = fields.Many2one('res.country', string="Country")
    tutor_id = fields.Many2one('university.teacher', string="Tutor")
    enrollment_ids = fields.One2many('university.enrollment', 'student_id', string="Enrollments")
    grade_ids = fields.One2many('university.grade', 'student_id', string="Grades")
