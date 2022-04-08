# coding: utf-8

from odoo import models, fields


class HrPayslipStructure(models.Model):
    _inherit = 'hr.payroll.structure'

    domain = "[('name','=', gross_daily_id.struct_id.name)]"

    cnaps_employer_id = fields.Many2one('hr.salary.rule', 'CNAPS employer',
                                        domain="[('struct_id.id','=', id)]")
    ostie_employer_id = fields.Many2one('hr.salary.rule', 'OSTIE employer',
                                        domain="[('struct_id.id','=', id)]")
    cnaps_id = fields.Many2one('hr.salary.rule', 'CNAPS employee', domain="[('struct_id.id','=', id)]")
    ostie_id = fields.Many2one('hr.salary.rule', 'OSTIE employee', domain="[('struct_id.id','=', id )]")
    fmfp_id = fields.Many2one('hr.salary.rule', 'FMFP', domain="[('struct_id.id','=', id)]")
    irsa_id = fields.Many2one('hr.salary.rule', 'IRSA', domain="[('struct_id.id','=', id)]")
    gross_salary_id = fields.Many2one('hr.salary.rule', 'Gross salary',
                                      domain="[('struct_id.id','=', id)]")
    net_salary_id = fields.Many2one('hr.salary.rule', 'Net salary', domain="[('struct_id.id','=', id)]")
    advantage_ids = fields.Many2many('hr.salary.rule.category', string='Advantage category')
    additional_hour_id = fields.Many2one('hr.salary.rule.category', string='Additional Hour')
    workday_code = fields.Char('Worked days code')
    gross_daily_id = fields.Many2one('hr.salary.rule', 'Gross daily salary',
                                     domain="[('struct_id.id','=', id)]")
