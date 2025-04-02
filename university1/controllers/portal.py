from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class GradesPortal(CustomerPortal):

    @http.route(['/my/grades'], type='http', auth="user", website=True)
    def portal_my_grades(self):
        grades = request.env['university.grade'].sudo().search([], order='date desc')
        values = {
            'page_name': 'grades',
            'grades': grades,
        }
        return request.render("university1.portal_my_grades", values)