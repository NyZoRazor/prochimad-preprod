# coding: utf-8

from odoo import models

MONTHS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def get_gross_salary_amount(self):
        """
        Method to get gross salary amount.
        :param payslip:
        :return: gross salary
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(
                    lambda p: p.salary_rule_id.code == rec.struct_id.gross_salary_id.code
                ).mapped('amount')
            )
        return total_amount

    def get_gross_daily_wage(self):
        """
        Get gross daily wage
        :return:
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(
                    lambda p: p.salary_rule_id.code == rec.struct_id.gross_daily_id.code
                ).mapped('amount')
            )
        return total_amount

    def get_fmfp(self):
        """
        Method to get fmfp.
        :return: fmfp
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(lambda p: p.salary_rule_id.code == rec.struct_id.fmfp_id.code).mapped('amount')
            )
        return total_amount

    def get_cnaps_employee(self):
        """
        Method to get cnaps employee.
        :return: cnaps employee
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(lambda p: p.salary_rule_id.code == rec.struct_id.cnaps_id.code).mapped('amount')
            )
        return total_amount

    def get_cnaps_employer(self):
        """
        Method to get cnaps employer.
        :return: cnaps employer
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(
                    lambda p: p.salary_rule_id.code == rec.struct_id.cnaps_employer_id.code
                ).mapped('amount')
            )
        return total_amount

    def get_ostie_employee(self):
        """
        Method to get ostie employee.
        :return: ostie employee
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(lambda p: p.salary_rule_id.code == rec.struct_id.ostie_id.code).mapped('amount')
            )
        return total_amount

    def get_ostie_employer(self):
        """
        Method to get ostie employer.
        :return: ostie employer
        """
        return sum(
            self.line_ids.filtered(lambda p: p.salary_rule_id.code == self.struct_id.ostie_employer_id.code).mapped(
                'amount'))

    def get_advantages_sum(self):
        """
        Method to get the sum of an employee advantages.
        :param payslip:
        :return: Advantage
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.line_ids.filtered(
                    lambda p: p.salary_rule_id.category_id.code in rec.struct_id.advantage_ids.mapped('code')
                ).mapped('amount')
            )
        return total_amount

    def get_workdays(self):
        """
        Get work days
        :return:
        """
        total_amount = 0
        for rec in self:
            total_amount += sum(
                rec.worked_days_line_ids.filtered(
                    lambda w: w.code == rec.struct_id.workday_code
                ).mapped('number_of_days')
            )
        return total_amount

    def get_wages_by_month(self, state_id):
        """
        Get wages (brut) by month
        :param state_id:
        :return:
        """
        months = MONTHS[int(state_id.quarter)]
        wages = {0: 0, 1: 0, 2: 0}
        for key, month in enumerate(months):
            payslip_ids = self.filtered(lambda p: int(p.date_to.month) == month)
            wages[key] = payslip_ids.get_gross_salary_amount()
        return wages

    def get_effectif_per_month(self, state_id):
        """
        Get payslip effectif in month
        :param state_id:
        :return:
        """
        months = MONTHS[int(state_id.quarter)]
        effectifs = {0: 0, 1: 0, 2: 0}
        for key, month in enumerate(months):
            payslip_ids = self.filtered(lambda p: int(p.date_to.month) == month)
            effectifs[key] = len(payslip_ids.mapped('employee_id'))
        return effectifs