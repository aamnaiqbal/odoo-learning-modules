# academy/models/academy_course.py
from odoo import models, fields

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
