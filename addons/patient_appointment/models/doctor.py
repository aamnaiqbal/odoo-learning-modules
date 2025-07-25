from odoo import models, fields

class Doctor(models.Model):
    _name = 'doctor.app'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
