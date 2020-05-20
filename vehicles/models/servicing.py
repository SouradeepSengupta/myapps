# -*- coding: utf-8 -*-

from odoo import models, fields


class vehicles_servicing(models.Model):
    _name = 'vehicles.servicing'

    name = fields.Char()
    number = fields.Integer()
    cost = fields.Float()
