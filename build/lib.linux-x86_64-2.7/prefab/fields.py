#------------------------------------------------------------------------------
#   file:       podunk/prefab/fields.py
#   author:     Jim Storch
#------------------------------------------------------------------------------

from widget.field import Field
from prefab.styles import HEADER_STYLE
from prefab.boxes import HEADER_BOX

## You need to do a copy.copy(FIELD_NAME) in order to use a prefab field in
## multiple spots

HEADER_FIELD = Field()
HEADER_FIELD.style = HEADER_STYLE
HEADER.box = HEADER_BOX
