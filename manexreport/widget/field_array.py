#------------------------------------------------------------------------------
#   file:       podunk/widget/field.py
#   author:     Jim Storch
#------------------------------------------------------------------------------

from manexreport.widget.box import Box

from manexreport.prefab.formats import format_plain
from manexreport.widget.style_array import StyleArray


class FieldArray(object):

    def __init__(self, value=None, style=None, box=None, format=None, width=72, 
            height=11):

        self.value = value
        self.width = width
        self.height = height

        if style:
            self.style = style
        else:
            self.style = StyleArray()

        if box:
            self.box = box
        else:
            self.box = Box()

        if format:
            self.format = format
        else:
            self.format = format_plain
    
    #------------------------------------------------------------------Set Size    

    def set_size(self, width, height):
        self.width = width
        self.height = height

    #-----------------------------------------------------------------Get Width

    def get_width(self, canvas):
        text = self.value #self.format(self.value)
        return self.style.get_width(canvas, text)       

    #----------------------------------------------------------------Get Height

    def get_height(self):
        return self.style.get_height() 

    #------------------------------------------------------------Get Dimensions

    def get_dimensions(self, canvas):
        width = self.get_width(canvas)
        height = self.get_height()
        return width,height

    #----------------------------------------------------------------------Draw

    def draw(self, canvas, x, y):
        text = self.value #self.format(self.value)
        self.box.draw(canvas, x, y, self.width, self.height)
        self.style.draw(canvas, text, x, y, self.width, self.height)