# -*- coding: utf-8 -*-

from odoo import models, fields


class vehicles(models.Model):
    _name = 'vehicles.vehicles'

    name = fields.Char()
    company = fields.Char()
    price = fields.Integer()
    registration_number = fields.Char()
    date_of_registration = fields.Date()
    description = fields.Text()
    need_servicing = fields.Boolean("Needs servicing ?")
