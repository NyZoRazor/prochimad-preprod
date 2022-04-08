from odoo import models, fields


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    name = fields.Char(string="Catégorie Partenaire")
    comm = fields.Float(
        string='Commission')

    payment_dt = fields.Datetime(string="date de payment")

    def _select(self):
        return super(AccountInvoiceReport, self)._select() +  """, categ.name, line.commission as comm, 
            move.payment_date as payment_dt"""

    def _from(self):
        return super(AccountInvoiceReport, self)._from() + """
            left join res_partner_res_partner_personalized_category_rel rel on partner.id = rel.res_partner_id
            left join res_partner_personalized_category categ on rel.res_partner_personalized_category_id = categ.id"""

