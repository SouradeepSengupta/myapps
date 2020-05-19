# -*- coding: utf-8 -*-

from odoo import models, fields


class vehicles_company(models.Model):
    _name = 'vehicles.company'

    name = fields.Char()
    registration_number = fields.Char()
    date_of_registration = fields.Date()
    description = fields.Text()
