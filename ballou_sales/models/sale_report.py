from odoo import fields, models, api


class SaleReport(models.Model):
    _inherit = "sale.report"

    commission = fields.Float(string="Commission", related="categ_id.commission")