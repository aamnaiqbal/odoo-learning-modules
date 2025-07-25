from odoo import models, fields

class Appointment(models.Model):
    _name = 'appointment.app'
    _description = 'Appointment'

    patient_id = fields.Many2one('patient.app', string='Patient', required=True)
    doctor_id = fields.Many2one('doctor.app', string='Doctor', required=True)
    date = fields.Datetime(string='Appointment Date', required=True)
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='scheduled', string='Status')
    notes = fields.Text(string='Notes')
