from odoo import models, fields

class Patient(models.Model):
    _name = 'patient.app'
    _description = 'Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Phone')
