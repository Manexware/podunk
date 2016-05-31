#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
from manexreport.prefab import alignment
from manexreport.prefab.formats import format_two_decimals
from manexreport.prefab.formats import format_us_currency
from manexreport.project.report import Report
from manexreport.widget.pagebreak import PageBreak
from manexreport.widget.table import Table

import manexreport.prefab.paper as paper
from manexreport.widget.heading_array import HeadingArray

table = Table()

col = table.add_column('employee')

col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('employee')
col.row.format = format_two_decimals
col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('employee')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('employee')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT


for x in range(10):
    table.add_row(['Smith, John', 10.0, 80.0, 800.0, ])

#table.count_column('employee', 8)
#table.average_column('employee', 1)
#table.sum_column('employee', 2)
#table.sum_column('employee', 3)
table.bold_column('employee', 2)

table2 = Table()

col = table2.add_column('employee')

col.row.style.horizontal_alignment = alignment.RIGHT

col = table2.add_column('employee')
col.row.format = format_two_decimals
col.row.style.horizontal_alignment = alignment.RIGHT

col = table2.add_column('employee')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT

col = table2.add_column('employee')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT


for x in range(10):
    table2.add_row(['Smith, John', 10.0, 80.0, 800.0, ])

#table.count_column('employee', 8)
#table.average_column('employee', 1)
#table.sum_column('employee', 2)
#table.sum_column('employee', 3)
table2.bold_column('employee', 1)

# pdf_file=None,
# paper_type=None,
# time_zone=None,
# left_margin=None,
# top_margin=None,
# right_margin=None,
# bottom_margin=None,
# date_flag=None,
# flag_footer=None,
# logo=None,
# logo_filename=None,
# logo_width=None,
# logo_height=None):
report = Report('demo.pdf',
                paper.A4_PORTRAIT,
                None,
                None,
                None,
                None,
                None,
                False,
                False,
                True,
                'python_logo.png',
                80,
                80,
                70)
report.title = ''
report.author = 'Manuel Vega'

line1_0 = 'CURSO :'
line1_1 = u'%s                             ' % 'CURSO DEMO'
line1_2 = u'PROMOCIÓN :'
line1_3 = u'%s  ' % 'ARMAS XL'
line1_4 = u'ANO: '
line1_5 = u'%s' % '2014'
text = [line1_0, line1_1, line1_2, line1_3, line1_4, line1_5]
heading = HeadingArray(text, 1, True, 14, alignment.LEFT, 4, False, False)

report.add(heading)
table.auto_grow(report.canvas, report.page_width - report.left_margin - report.right_margin)
table.set_drew_header(True)
table.set_flag(False)

report.add(table)
report.add(table2)
report.add(PageBreak())

report.create()