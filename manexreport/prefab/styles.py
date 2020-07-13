
###############################################################################
#   file:       podunk/prefab/styles.py
#   author:     Jim Storch
###############################################################################

from manexreport.prefab import alignment
from manexreport.widget.style import Style

# -------------------------------------------------------------------------Money

from  manexreport.prefab.fonts import DEJAVU_SANS_MONO

MONEY = Style()
MONEY.font = DEJAVU_SANS_MONO
MONEY.horizontal_alignment = alignment.RIGHT

# -------------------------------------------------------------------------Header

HEADER_STYLE = Style()
HEADER_STYLE.horizontal_alignment = alignment.RIGHT


