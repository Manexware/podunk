
###############################################################################
#   file:       podunk/widget/font.py
#   author:     Jim Storch
###############################################################################

# import os
# from reportlab.pdfbase import pdfmetrics

"""
This class is designed so that the report coder can treat built-in and embedded
fonts in exactly the same manner.  If you specify a path in the keyword dict
then it will load them from disk, otherwise it just holds names.
"""


def embed_font(path, face_name):
    """
    Register a font face with ReportLab an (if used) embed in the target PDF.
    """
    # Based on snippet from http://www.reportlab.org/devfaq.html
    # fm = os.path.join(path, face_name + '.afm')
    # pfb = os.path.join(path, face_name + '.pfb')
    # face = pdfmetrics.EmbeddedType1Face(afm, pfb)
    # pdfmetrics.registerTypeFace(face)
    # font = pdfmetrics.Font(face_name, face_name, 'WinAnsiEncoding')
    # pdfmetrics.registerFont(font)


class Font(object):

    def __init__(self, kwargs):

        self.plain = kwargs['plain']
        self.bold = kwargs['bold']
        self.italic = kwargs['italic']
        self.bold_italic = kwargs['bold_italic']

        if 'path' in kwargs:

            path = kwargs['path']

            if path:
                embed_font(path, self.plain)
                embed_font(path, self.bold)
                embed_font(path, self.italic)
                embed_font(path, self.bold_italic)

    # ------------------------------------------------------------Embed Font
