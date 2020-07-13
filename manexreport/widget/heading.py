
###############################################################################
#   file:       podunk/widget/heading.py
#   author:     Jim Storch
###############################################################################

from manexreport.prefab import alignment
from manexreport.widget.field import Field


class Heading(object):

    def __init__(self, value=None, vertical_padding=None, bold=None, size=None,
                 horizontal_alignment=None,
                 skip=None,
                 drew_skip=None,
                 drew_title=None):
    
        if value:
            self.field = Field(value)
        else:
            self.field = Field()

        if vertical_padding is not None:
            self.field.style.vertical_padding = vertical_padding
        else:
            self.field.style.vertical_padding = 2

        if bold:
            self.field.style.bold = True
        else:
            self.field.style.bold = bold

        if size is not None:
            self.field.style.size = size
        else:
            self.field.style.size = 10

        if horizontal_alignment:
            self.field.style.horizontal_alignment = horizontal_alignment
        else:
            self.field.style.horizontal_alignment = alignment.CENTER

        if skip is not None:
            self.skip = skip
        else:
            self.skip = 8

        if drew_skip:
            self._drew_skip = drew_skip
        else:
            self._drew_skip = True

        if drew_title:
            self._drew_title = drew_title
        else:
            self._drew_title = False

    # -------------------------------------------------------------------Add Field

    def get_field(self):
        return self.field

    # -----------------------------------------------------------------Draw Some

    def draw_some(self, canvas, left, right, yoff, vspace):

        if not self._drew_skip:
            height = self.skip
            if height < vspace:
                used = height
            else:
                used = vspace
            self._drew_skip = True

        elif not self._drew_title:
            height = self.field.get_height()
            # Is there enought room for the title?
            if height < vspace:
                self.field.width = right - left
                self.field.draw(canvas, left, yoff)
                self._drew_title = True
                used = height

            # If not, force a new page
            else:
                used = vspace
                
        # We're done
        else:
            used = 0

        return used
