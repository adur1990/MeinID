"""Module containing the default settings."""
import os

# Base path for module
BASE_DIR = os.path.dirname(__file__)

# VW user data (make sure to change it to correct data)
VW_USERNAME = 'volkswagen@artursterz.de'
VW_PASSWORD = 'YbM\~O\V`-kr:W79[;~W;*3Qs'

# known request prefixes
PREFIX_LIST = [185, 900, 877, 902] # known prefixes for ID.3/4/5

# skip requesting extra details for cars with VIN like line drawings
SKIP_VIN_DETAILS = True

# commission number range
COMMISSION_NUMBER_RANGE = [
    ('AF', 5000, 9999, 4),
    ('AG', 0, 9999, 4),
    ('AH', 0, 9999, 4),
    ('AI', 0, 9999, 4),
    ('AJ', 0, 9999, 4),
    ('AK', 0, 9999, 4),
    ('AL', 0, 9999, 4),
    ('AM', 0, 9999, 4)
]
