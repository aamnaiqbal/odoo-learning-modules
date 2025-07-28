from odoo import models, fields

class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Hospital Department'

    name = fields.Char()
    description = fields.Text()
    doctor_ids = fields.One2many('hospital.doctor', 'department_id')

