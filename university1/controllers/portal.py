from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class GradesPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        
        # Check if current user is linked to a student
        student = request.env['university.student'].sudo().search([('user_id', '=', request.env.user.id)], limit=1)
        values['show_grades'] = bool(student)
        
        if 'grades_count' in counters:
            values['grades_count'] = len(student.grade_ids) if student else 0
            
        return values

    @http.route(['/my/grades'], type='http', auth="user", website=True)
    def portal_my_grades(self):
        # Get student record for current user
        student = request.env['university.student'].sudo().search([('user_id', '=', request.env.user.id)], limit=1)
        
        if not student:
            return request.redirect('/my')
            
        grades = request.env['university.grade'].sudo().search([
            ('student_id', '=', student.id)
        ], order='date desc')
        
        values = {
            'page_name': 'grades',
            'grades': grades,
        }
        return request.render("university1.portal_my_grades", values)