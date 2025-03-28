from odoo import models, fields

class University(models.Model):
    _name = 'university.university'
    _description = 'University'

    name = fields.Char(string="Name", required=True)
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Postal Code")
    state_id = fields.Many2one('res.country.state', string="State")
    country_id = fields.Many2one('res.country', string="Country")
    director_id = fields.Many2one('university.teacher', string="Director")

    department_ids = fields.One2many('university.department', 'university_id', string="Departments")
    teacher_ids = fields.One2many('university.teacher', 'university_id', string="Teachers")
    student_ids = fields.One2many('university.student', 'university_id', string="Students")
    enrollment_ids = fields.One2many('university.enrollment', 'university_id', string="Enrollments")
