from odoo import models, fields

class HospitalDoctorSchedule(models.Model):
    _name = 'hospital.doctor.schedule'
    _description = 'Doctor Weekly Availability'
    _order = 'day, start_time'

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True, ondelete='cascade')
    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ], string='Day', required=True)
    start_time = fields.Float(string='Start Time', required=True, help='24-hour format (e.g. 13.5 = 1:30 PM)')
    end_time = fields.Float(string='End Time', required=True, help='24-hour format (e.g. 15.0 = 3:00 PM)')
