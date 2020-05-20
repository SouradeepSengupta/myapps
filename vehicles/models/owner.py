# -*- coding: utf-8 -*-

from odoo import models, fields


class vehicles_owner(models.Model):
    _inherit = 'res.partner'

    demo_done = fields.Boolean()
    sales_person = fields.Many2one('res.users')
    vehicles = fields.One2many('vehicles.vehicles', 'owner')
