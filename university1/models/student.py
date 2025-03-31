from odoo import models, fields, api

class Student(models.Model):
    _name = 'university.student'
    _description = 'Student'

    image = fields.Image(string="Image", max_width=1920, max_height=1920)
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

    # Counted fileds for the counters and their functions
    enrollments_count = fields.Integer(compute='_compute_enrollments_count', string='Enrollments Count')
    grades_count = fields.Integer(compute='_compute_grades_count', string='Grades Count')

    def _compute_enrollments_count(self):
        for student in self:
            student.enrollments_count = self.env['university.enrollment'].search_count([('student_id', '=', student.id)])

    def _compute_grades_count(self):
        for student in self:
            student.grades_count = self.env['university.grade'].search_count([('student_id', '=', student.id)])

    def action_view_enrollments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Enrollments',
            'res_model': 'university.enrollment',
            'view_mode': 'list,form',
            'domain': [('student_id', '=', self.id)],
            'context': {'default_student_id': self.id}
        }

    def action_view_grades(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Grades',
            'res_model': 'university.grade',
            'view_mode': 'list,form',
            'domain': [('student_id', '=', self.id)],
            'context': {'default_student_id': self.id}
        }