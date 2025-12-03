# FunGraphics - Simple import helper
# Place this file in the same directory as your Python script

import sys
import os

# Automatically add the src directory to the path
_current_dir = os.path.dirname(os.path.abspath(__file__))
_src_dir = os.path.join(_current_dir, 'src')
if os.path.exists(_src_dir) and _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

# Now you can simply import
from fungraphics import *
