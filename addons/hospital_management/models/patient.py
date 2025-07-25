from odoo import fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"  # Table name in db: hospital_patient
    _description = "Patient" #Human-friendly name of the model, shown in the UI.

    name = fields.Char(string= "Patient Name")  # Field for patient's name
    age = fields.Integer(string = "Age")  # Field for patient's age
    gender= fields.Selection([('male', "Male"),('female', "Female"),('other', "Other")], string= "Gender")
