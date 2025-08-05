from odoo import models, fields

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Patient Appointment'

    patient_name = fields.Char(string='Patient Name', required=True)
    phone = fields.Char(string='Phone')
    appointment_date = fields.Date(string='Appointment Date')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
