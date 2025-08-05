from odoo import fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one("hospital.patient", string="Patient", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    note = fields.Text(string="Note")
