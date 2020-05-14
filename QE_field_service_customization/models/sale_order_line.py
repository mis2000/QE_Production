# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _timesheet_create_task_prepare_values(self, project):
        ''' Here we assign start date, enddate and assignd user in related task.'''
        taskValues = super(SaleOrderLine, self)._timesheet_create_task_prepare_values(project)
        commitmentDate = fields.Datetime.from_string(
                        self.order_id.commitment_date if self.order_id.commitment_date else fields.Datetime.now())
        taskValues.update({
            'planned_date_begin': commitmentDate,
            'planned_date_end': commitmentDate + timedelta(minutes = 15),
            'user_id': self.order_id.user_id and self.order_id.user_id.id or False,
            })
        return taskValues
