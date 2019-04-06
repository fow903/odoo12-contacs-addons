#-*- coding: utf-8 -*-
from odoo import models, fields

class ExtraFields(models.Model):
    _inherit = 'res.partner'
    phone_2 = fields.Char('Teléfono 2')
    ext = fields.Char('Extensión')
    email_2 = fields.Char('Email 2')

class CatchInherit(models.Model):
    _inherit = 'res.partner'
    catchment_id = fields.Many2one('catchment.method', string='Catchment Method')

class PartnerInherit(models.Model):
    _inherit = 'catchment.method'
    part_id = fields.One2many('res.partner', 'catchment_id')