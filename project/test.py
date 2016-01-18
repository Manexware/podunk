#!/usr/bin/env python
from project.report import Report
from widget.table import Table
from widget.heading import Heading
from prefab import alignment
from prefab.formats import format_us_currency
from prefab.formats import format_two_decimals

table = Table()

col = table.add_column('employee')

col = table.add_column('rate')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('hours')
col.row.format = format_two_decimals
col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('pay')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT

for x in range(10):
    table.add_row(['Smith, John', 10.0, 80.0, 800.0, ])

table.count_column('employee')
table.average_column('rate')
table.sum_column('hours')
table.sum_column('pay')

report = Report('test.pdf')
report.title = 'Payroll for July 18, 2008'
report.author = 'Test Script'
report.add(Heading('A Sample Payroll'))
report.add(table)
report.create()