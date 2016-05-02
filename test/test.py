#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
from manexreport.prefab import alignment
from manexreport.prefab.formats import format_two_decimals
from manexreport.prefab.formats import format_us_currency
from manexreport.project.report import Report
from manexreport.widget.pagebreak import PageBreak
from manexreport.widget.table import Table

import manexreport.prefab.paper as paper
from manexreport.widget.heading import Heading

table = Table()

col = table.add_column('employee')

col = table.add_column('employee')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('employee')
col.row.format = format_two_decimals
col.row.style.horizontal_alignment = alignment.RIGHT

col = table.add_column('employee')
col.row.format = format_us_currency
col.row.style.horizontal_alignment = alignment.RIGHT


for x in range(10):
    table.add_row(['Smith, John', 10.0, 80.0, 800.0, ])

table.count_column('employee', 8)
table.average_column('employee', 1)
table.sum_column('employee', 2)
table.sum_column('employee', 3)

#pdf_file=None, paper_type=None, time_zone=None, left_margin=None, top_margin=None,
#right_margin=None, bottom_margin=None, logo=None, logo_filename=None, logo_x=None, logo_y=None,
#logo_width=None, logo_height=None
report = Report('demo.pdf', paper.A4_PORTRAIT,None,None,None,None,None,False, True,'python_logo.png', 80, 80)
report.title = ''
report.author = 'Manuel Vega'
heading = Heading('ACADEMIA DE GUERRA NAVAL', 1, True, 14, alignment.CENTER, 4, False, False)

report.add(heading)
report.add(table)
report.add(PageBreak())
report.create()