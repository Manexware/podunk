
###############################################################################
#   file:       podunk/prefab/fields.py
#   author:     Jim Storch
###############################################################################

from manexreport.prefab.boxes import HEADER_BOX
from manexreport.prefab.styles import HEADER_STYLE
from manexreport.widget.field import Field

# You need to do a copy.copy(FIELD_NAME) in order to use a prefab field in
# multiple spots

HEADER_FIELD = Field()
HEADER_FIELD.style = HEADER_STYLE
HEADER_FIELD.box = HEADER_BOX
