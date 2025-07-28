from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()
    specialization = fields.Char()
    image = fields.Image()
    bio = fields.Text()
    department_id = fields.Many2one('hospital.department')