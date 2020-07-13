
###############################################################################
#   file:       podunk/project/report.py
#   author:     Jim Storch, Manuel Vega
###############################################################################

import datetime

import pytz
from manexreport.prefab import alignment
from manexreport.prefab.formats import format_report_date
from reportlab.pdfgen.canvas import Canvas
from manexreport.prefab import paper
from manexreport.widget.field import Field


class Report(object):
    def __init__(self,
                 pdf_file=None,
                 paper_type=None,
                 time_zone=None,
                 left_margin=None,
                 top_margin=None,
                 right_margin=None,
                 bottom_margin=None,
                 date_flag=None,
                 flag_footer=None,
                 logo=None,
                 logo_filename=None,
                 logo_width=None,
                 logo_height=None,
                 logo_top_margin=None):

        self.pdf_file = pdf_file
        self.title = ''
        self.author = 'Manexware S.A.'
        self.department = 'OpenEduNav'
        self.date_flag = date_flag
        self.logo = logo
        self.logo_filename = logo_filename
        self.logo_width = logo_width
        self.logo_height = logo_height
        self.flag_footer = flag_footer

        if time_zone:
            local_tz = pytz.timezone(time_zone)
        else:
            local_tz = pytz.timezone('America/Guayaquil')
        utc_dt = datetime.datetime.utcnow()
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
        date_time = local_tz.normalize(local_dt)

        if paper_type:
            self.page_width, self.page_height = paper_type
        else:
            self.page_width, self.page_height = paper.A4_LANDSCAPE

        if left_margin is not None:
            self.left_margin = left_margin
        else:
            self.left_margin = 50

        if top_margin is not None:
            self.top_margin = top_margin
        else:
            self.top_margin = 40

        if right_margin is not None:
            self.right_margin = right_margin
        else:
            self.right_margin = 50

        if bottom_margin is not None:
            self.bottom_margin = bottom_margin
        else:
            self.bottom_margin = 40
        if logo_top_margin is not None:
            self.logo_top_margin = logo_top_margin
        else:
            self.logo_top_margin = 70

        # Metrics
        self._top_edge = self.page_height - 1
        self._right_edge = self.page_width - 1
        self._bottom_edge = 0
        self._left_edge = 0
        self._working_width = self.page_width - (
            self.right_margin + self.left_margin)
        self._working_height = self.page_height - (
            self.top_margin + self.bottom_margin)

        # Create the ReportLab Canvas
        self.canvas = Canvas(self.pdf_file, pagesize=(self.page_width, self.page_height))

        # Create the page header
        self.header = Field()
        # self.header.box.bottom_border = 2
        # self.header.box.line_cap = 1
        # self.header.box.border_color = (.6,.6,.6)
        self.header.style.vertical_padding = 6
        self.header.style.bold = True
        self.header.style.size = 10
        # self.header.style.color = (.6,.6,.6)
        self.header.style.horizontal_alignment = alignment.RIGHT
        self.header.width = self._working_width

        # Create the page footer
        self.footer = Field()
        self.footer.box.top_border = 1
        self.footer.box.line_cap = 1
        # self.footer.box.border_color = (.6,.6,.6)
        self.footer.style.horizontal_alignment = alignment.CENTER
        self.footer.style.vertical_alignment = alignment.TOP
        # self.footer.style.color = (.6,.6,.6)
        self.footer.width = self._working_width
        self.footer.style.size = 8

        # Create the date label
        self.date = Field(date_time)
        self.date.format = format_report_date
        self.date.style.vertical_alignment = alignment.TOP
        # self.date.style.color = (.6,.6,.6)
        # self.date.style.horizontal_padding = 0
        self.date.style.size = 9

        # Create the department label
        self.departmentField = Field()
        self.departmentField.style.vertical_alignment = alignment.TOP
        # self.date.style.color = (.6,.6,.6)
        # self.date.style.horizontal_padding = 0
        self.departmentField.style.size = 8

        # Create the page number label; 'Page X of'
        self.page_num = Field()
        self.page_num.style.horizontal_alignment = alignment.RIGHT
        self.page_num.style.vertical_alignment = alignment.TOP
        self.page_num.width = self._working_width - 13
        # self.page_num.style.color = (.6,.6,.6)
        self.page_num.horizontal_padding = 0
        self.page_num.style.size = 8

        # Create the last page number label
        self.last_page = Field()
        # self.last_page.style.horizontal_alignment = alignment.LEFT
        self.last_page.style.vertical_alignment = alignment.TOP
        # self.last_page.width = self._working_width
        # self.last_page.style.color = (.6,.6,.6)
        self.last_page.horizontal_padding = 0
        self.last_page.style.size = 8

        # Objects to be drawn
        self.draw_list = []

        self._page_count = 1

    # -----------------------------------------------------------------------Add

    def add(self, item):
        # Add any object that, duck-typingly, has a 'draw_some' method
        self.draw_list.append(item)

    # --------------------------------------------------------------------Create

    def create(self):
        self.canvas.setAuthor(self.author)
        self.canvas.setTitle(self.title)
        self.canvas.setSubject('Python Generated Report')
        self._draw_header()
        if self.flag_footer:
            self._draw_footer()
        vspace = self._working_height
        left = self.left_margin
        right = self.page_width - self.right_margin

        if self.logo:
            self._draw_logo()
            vspace = self._working_height - self.logo_height

        for item in self.draw_list:

            while True:

                if vspace < 1:
                    self._start_new_page()
                    if self.logo:
                        vspace = self._working_height - self.logo_height
                    else:
                        vspace = self._working_height

                yoff = self.bottom_margin + vspace
                used = item.draw_some(self.canvas, left, right, yoff, vspace)

                if used == 0:
                    break

                else:
                    vspace -= used

        # Add the numbering for last page
        # We have to do this as a PDF 'Form' object since we don't know in
        # advance how many pages there will be.
        self.canvas.beginForm('last_page')
        self.canvas.saveState()
        self.last_page.value = '%d' % self._page_count
        self.last_page.draw(self.canvas,
                            self._right_edge - (self.right_margin + 14),
                            self.bottom_margin * .65)
        self.canvas.restoreState()
        self.canvas.endForm()

        # Close the PDF
        self.canvas.save()

    # ----------------------------------------------------------------Start Page

    def _start_new_page(self):
        self._page_count += 1
        self.canvas.showPage()
        # self.canvas.doForm('page %s' % self._page_count)
        self._draw_header()
        if self.flag_footer:
            self._draw_footer()
        if self.logo:
            self._draw_logo()

    # ---------------------------------------------------------------Draw Header

    def _draw_header(self):
        self.header.value = self.title
        self.header.draw(self.canvas, self.left_margin, self._top_edge - (self.top_margin * .65))
        if self.date_flag:
            self.date.draw(self.canvas, self._right_edge - 200, self._top_edge - (self.top_margin * .65))

    # ---------------------------------------------------------------Draw Logo

    def _draw_logo(self):
        if self.logo:
            x = ((self.page_width - self.logo_width) / 2)
            y = self._top_edge - self.logo_top_margin
            self.canvas.drawImage(self.logo_filename, x, y, self.logo_width, self.logo_height)

    # ---------------------------------------------------------------Draw Footer

    def _draw_footer(self):
        self.footer.value = self.author
        self.footer.draw(self.canvas, self.left_margin, self.bottom_margin * .65)
        self.departmentField.value = self.department
        self.departmentField.draw(self.canvas, self.left_margin, self.bottom_margin * .65)
        self.page_num.value = 'Página No. %d de ' % self._page_count
        self.page_num.draw(self.canvas, self.left_margin, self.bottom_margin * .65)
        self.canvas.doForm('last_page')