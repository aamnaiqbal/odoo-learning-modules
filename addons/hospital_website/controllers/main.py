from odoo import http
from odoo.http import request

class HospitalWebsite(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('hospital_website.homepage_template')

    @http.route('/departments', type='http', auth='public', website=True)
    def departments(self, **kwargs):
        departments = request.env['hospital.department'].sudo().search([])
        return request.render('hospital_website.departments_template', {
            'departments': departments
        })

    @http.route('/doctors', type='http', auth='public', website=True)
    def doctors_page(self, **kwargs):
        doctors = request.env['hospital.doctor'].sudo().search([])
        return request.render('hospital_website.doctors_template', {
            'doctors': doctors
        })

    @http.route('/doctors/<int:dept_id>', type='http', auth='public', website=True)
    def doctors_by_department(self, dept_id, **kwargs):
        doctors = request.env['hospital.doctor'].sudo().search([('department_id', '=', dept_id)])
        department = request.env['hospital.department'].sudo().browse(dept_id)
        return request.render('hospital_website.doctors_template', {
            'doctors': doctors,
            'department': department
        })
    
    @http.route('/hospital/appointment', type='http', auth='public', website=True)
    def appointment_form(self, **kwargs):
        doctors = request.env['hospital.doctor'].sudo().search([])
        return request.render('hospital_website.patient_appointment_form', {
            'doctors': doctors
        })

    @http.route('/hospital/appointment/submit', type='http', auth='public', methods=['POST'], website=True)
    def appointment_submit(self, **post):
        request.env['hospital.appointment'].sudo().create({
            'patient_name': post.get('name'),
            'phone': post.get('phone'),
            'appointment_date': post.get('date'),
            'doctor_id': int(post.get('doctor_id')) if post.get('doctor_id') else False
        })
        return request.redirect('/hospital/appointment/thankyou')

    @http.route('/hospital/appointment/thankyou', type='http', auth='public', website=True)
    def appointment_thankyou(self, **kwargs):
        return request.render('hospital_website.appointment_thankyou')
