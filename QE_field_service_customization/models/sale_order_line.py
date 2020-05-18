# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    start_job_date = fields.Datetime(string='Job Start Date', default=fields.Datetime.now, help="Schedule Start date.")
    end_job_date = fields.Datetime(string='Job End Date', help="Schedule Start date.")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _timesheet_create_task_prepare_values(self, project):
        ''' Here we assign start date, enddate and assignd user in related task.'''
        taskValues = super(SaleOrderLine, self)._timesheet_create_task_prepare_values(project)
        startDate = self.order_id.start_job_date.replace(second=0) if self.order_id.start_job_date else fields.Datetime.now().replace(second=0)
        taskValues.update({
            'planned_date_begin': startDate,
            'planned_date_end': self.order_id.end_job_date.replace(second=0) if self.order_id.end_job_date else startDate + timedelta(minutes=15),
            'user_id': self.order_id.user_id and self.order_id.user_id.id or False,
            })
        return taskValues
