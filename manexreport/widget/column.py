
###############################################################################
#   file:       podunk/widget/column.py
#   author:     Jim Storch
###############################################################################

from manexreport.prefab.formats import format_title

from manexreport.prefab import alignment
from manexreport.widget.field import Field


class Column(object):

    def __init__(self, name, width=None):

        self.name = name
        self.value_list = []

        if width:
            self.width = width
        else:
            self.width = 72

        self.height = 9

        # Header
        self.header = Field(name)
        self.header.format = format_title
        self.header.style.bold = True
        self.header.style.color = (1,1,1)
        self.header.style.horizontal_alignment = alignment.CENTER
        # self.header.box.bottom_border = 1
        self.header.box.background_color = (0,0,0)

        # Row
        self.row = Field()
        self.row.style.bold = False

        # Footer
        self.footer = Field()
        self.footer.style.bold = True
        self.footer.box.top_border = 1         
        self.footer.style.horizontal_alignment = alignment.CENTER
        self.footer.value = None

    # --------------------------------------------------------------------Append

    def append(self, value):
        self.value_list.append(value)

    # ---------------------------------------------------------------Draw Header

    def draw_header(self, canvas, x, y):
        self.header.width = self.width
        self.header.height = self.height
        self.header.draw(canvas, x, y)

    # ------------------------------------------------------------------Draw Row

    def draw_row(self, canvas, x, y, row_number, flag, row_number_flag):

        if row_number % 2 and flag:
            self.row.box.background_color = (.9, .9, .9)
        else:
            self.row.box.background_color = (1,1,1)

        self.row.value = self.value_list[row_number]
        if row_number in row_number_flag:
            self.row.style.bold = True
        else:
            self.row.style.bold = False
        self.row.width = self.width
        self.row.height = self.height
        self.row.draw(canvas, x, y)

    # ---------------------------------------------------------------Draw Footer

    def draw_footer(self, canvas, x, y):
        if self.footer.value is not None:
            self.footer.width = self.width
            self.footer.height = self.height
            self.footer.draw(canvas, x, y)

    # ----------------------------------------------------------------Find Width
    
    def find_width(self, canvas):
        """
        Return the width of the widest element in this column.
        """
        widths = [self.header.get_width(canvas), self.footer.get_width(canvas)]
        for value in self.value_list:
            self.row.value = value
            widths.append(self.row.get_width(canvas))
        return max(widths)
    
    # ----------------------------------------------------------------Auto Width
    
    def auto_width(self, canvas):
        """
        Set the column width to the widest element found.
        """
        self.width = self.find_width(canvas)
