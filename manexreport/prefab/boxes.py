
###############################################################################
#   file:       podunk/prefab/boxes.py
#   author:     Jim Storch
###############################################################################

from manexreport.prefab import color
from manexreport.prefab import line
import manexreport.widget.box as box

# ---------------------------------------------------------------------Blank Box

BLANK_BOX = box.Box()

# -------------------------------------------------------------------Grey Square

GREY_SQUARE = box.Box()
GREY_SQUARE.left_border = 1
GREY_SQUARE.top_border = 1
GREY_SQUARE.right_border = 1
GREY_SQUARE.bottom_border = 1
GREY_SQUARE.background_color = color.LIGHT_GREY

# ----------------------------------------------------------------------Thin Box

THIN_BOX = box.Box()
THIN_BOX.left_border = .25
THIN_BOX.top_border = .25
THIN_BOX.right_border = .25
THIN_BOX.bottom_border = .25

# ----------------------------------------------------------------------Header Box

HEADER_BOX = box.Box()
HEADER_BOX.left_border = .25
HEADER_BOX.top_border = .25
HEADER_BOX.right_border = .25
HEADER_BOX.bottom_border = .25

# -----------------------------------------------------------------Dotted Bottom

DOTTED_BOTTOM = box.Box()
DOTTED_BOTTOM.bottom_border = 1
DOTTED_BOTTOM.border_color = color.GREY
DOTTED_BOTTOM.border_style = line.DOTTED
