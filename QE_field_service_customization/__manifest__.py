# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    'name': 'QE Field Service Customization',
    'summary': 'Customization in Field Service Management Application.',
    'description': """
        1) Display Customer name and city on top of task name in Kanban view.
        2) Display Customer name and city on top of task name in Calendar view.
        3) When Confirm Sale order then Start Date, End Date and Assigned to set in Task.
        4) Calendar view customization like add 15 minute time slot insted of 30 minute.

    """,
    'category': 'Operations/Field Service',
    'version': '13.0.1.0.0',
    'author': "Isarel Gross",
    'depends': ['web', 'industry_fsm', 'project', 'project_enterprise', 'sale_timesheet'],
    'data': [
        'views/webclient_templates.xml',
        'views/fsm_views.xml',
        'views/sale_views.xml',
    ],
    'qweb': [
        "static/src/xml/web_calendar.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
