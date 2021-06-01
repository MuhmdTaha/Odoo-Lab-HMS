# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ItiMansoura(models.Model):
    _name = 'iti.mansoura'
    _description = 'this is description'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', required=True, default='Ahmed', tracking=True)
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    float = fields.Float()
    boolean = fields.Boolean(default=True)
    html = fields.Html()
    selection = fields.Selection([('v1', 'Value 1'), ('v2', 'Value 2'), ('v3', 'Value 3')], default='v1')
    binary = fields.Binary()
    date = fields.Date()
    datetime = fields.Datetime()
    state = fields.Selection(
        [('new', 'New'), ('confirmed', 'Confirmed'), ('graduated', 'Graduated'), ('failed', 'Failed')], default='new')

    _sql_constraints = [
        ('key_uniq', 'check(1==1)', 'Name must be unique.')
    ]

    @api.constrains('value2')
    def _check_account_or_tags(self):
        if self.value2 > 200:
            raise ValidationError(_('value 2 must be less than 200'))

    # @api.onchange('value')
    # def on_change_value(self):
    #     self.float = self.value / 3

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def action_confirmed(self):
        # print('hello')
        # self.env['father'].create({
        #     'name': self.name,
        # })
        son_names = []
        search_res = self.env['father'].search([('son_ids', '!=', False)])
        for rec in search_res:
            rec.unlink()
        #     for son in rec.son_ids:
        #         son_names.append(son.name)
        # raise ValidationError(_(str(son_names).replace("\'", '').replace('[', '').replace(']', '')))

    def action_graduate(self):
        # print('hello')
        self.state = "graduated"


class Father(models.Model):
    _name = 'father'

    name = fields.Char()
    son_ids = fields.One2many('son', 'father_id')

    iti_id = fields.Many2one('iti.mansoura', domain="[('state','=','graduated'),('value','>',50)]")


class Son(models.Model):
    _name = 'son'

    name = fields.Char()
    father_id = fields.Many2one('father')

    #
