#------------------------------------------------------------------------------
#   file:       podunk/widget/style.py
#   author:     Jim Storch
#------------------------------------------------------------------------------

from manexreport.prefab import color
from manexreport.prefab import alignment
from manexreport.prefab.fonts import ARIAL


class StyleArray(object):

    def __init__(self):

        self.font = ARIAL
        self.bold = False
        self.italic = False
        self.size = 8
        self.horizontal_padding = 1
        self.vertical_padding = 1
        self.color = color.BLACK
        self.horizontal_alignment = alignment.LEFT
        self.vertical_alignment = alignment.BOTTOM

    #------------------------------------------------------------------Get Face

    def get_face(self):
        """
        Return the name of the current font, including bold/italic variants.
        """
        if self.bold and self.italic:
            face = self.font.bold_italic
        elif self.bold and not self.italic:
            face = self.font.bold
        elif not self.bold and self.italic:
            face = self.font.italic        
        else:
            face = self.font.plain
        return face
    
    #-----------------------------------------------------------------Get Width

    def get_width(self, canvas, text):
        """
        Return the width of a given string at current font face/size.
        Includes padding on the left and right.
        """
        face = self.font.bold
        data = ''
        for word in enumerate(text):
            data = '%s ' % word

        return canvas.stringWidth(data, face, self.size) + (
            self.horizontal_padding * 2)

    #----------------------------------------------------------------Get Height

    def get_height(self):
        """
        Return the height of a given string at current font size.
        Includes padding for the top and bottom.
        """     
        return self.size + (self.vertical_padding * 2)

    #------------------------------------------------------------Get Dimensions

    def get_dimensions(self, canvas, text):
        """
        Return the width and height of the given text at current font size.
        Includes padding on all sides.
        """
        width = self.get_width(canvas, text)
        height = self.get_height()
        return width,height

    #----------------------------------------------------------------------Draw

    def draw(self, canvas, text, x, y, width, height):
        
        canvas.saveState()

        ## Set the font characteristics      
        canvas.setFont(self.font.bold, self.size)
        canvas.setFillColor(self.color)

        ## Get the vertical alignment       
        if self.vertical_alignment == alignment.BOTTOM:
            y_off = y + self.vertical_padding

        elif self.vertical_alignment == alignment.TOP:
            y_off = ( y + height ) - ( self.vertical_padding + self.size)

        else: ## alignment.CENTERED
            y_off = y + ( ( height / 2 ) - ( self.size / 2 ) )

        ## Now the horizontal
        x_off = x + self.horizontal_padding
        for index, word in enumerate(text):
            canvas.drawString(x_off, y_off, word)
            if index % 2 == 0 :
                x_off += canvas.stringWidth(word, self.font.bold, self.size) + 2
                canvas.setFont(self.font.plain, self.size)
            else:
                x_off += canvas.stringWidth(word, self.font.plain, self.size) + 2
                canvas.setFont(self.font.bold, self.size)

        canvas.restoreState()