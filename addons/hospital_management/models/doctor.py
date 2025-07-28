from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialty = fields.Selection([
        ('cardiologist', 'Cardiologist'),
        ('dermatologist', 'Dermatologist'),
        ('pediatrician', 'Pediatrician'),
        ('neurologist', 'Neurologist'),
        ('orthopedic', 'Orthopedic Surgeon'),
        ('gynecologist', 'Gynecologist'),
        ('oncologist', 'Oncologist'),
        ('psychiatrist', 'Psychiatrist'),
        ('endocrinologist', 'Endocrinologist'),
        ('gastroenterologist', 'Gastroenterologist'),
        ('ophthalmologist', 'Ophthalmologist'),
        ('ent', 'ENT Specialist'),
        ('urologist', 'Urologist'),
        ('nephrologist', 'Nephrologist'),
        ('pulmonologist', 'Pulmonologist'),
        ('rheumatologist', 'Rheumatologist'),
        ('general_physician', 'General Physician'),
    ], string='Specialty', required=True)
    gender = fields.Selection([
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ], string='Gender')
    contact_number = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    experience_years = fields.Integer(string='Years of Experience')
    profile_image = fields.Image(string='Profile Image')
    schedule_ids = fields.One2many('hospital.doctor.schedule', 'doctor_id', string='Weekly Availability')
    consultation_fee = fields.Float(string='Consultation Fee')
    online_consultation = fields.Boolean(string='Online Consultation Available')
    bio = fields.Text(string='Short Bio')
