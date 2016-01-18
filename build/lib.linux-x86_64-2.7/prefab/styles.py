#------------------------------------------------------------------------------
#   file:       podunk/prefab/styles.py
#   author:     Jim Storch
#------------------------------------------------------------------------------

from widget.style import Style
from prefab import color
from prefab import alignment

#-------------------------------------------------------------------------Money

from prefab.fonts import DEJAVU_SANS_MONO
MONEY = Style()
MONEY.font = DEJAVU_SANS_MONO
MONEY.horizontal_alignment = alignment.RIGHT


