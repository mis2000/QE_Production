odoo.define('QE_field_service_customization.calendar', function (require) {
"use strict";

    var CalendarView = require('web.CalendarView');

    var Calendar = CalendarView.include({
        jsLibs: ['/QE_field_service_customization/static/src/js/fullcalendar.js'],
    });

});