# FunGraphics - Single-File Version

**One file. Zero setup. Start coding in seconds!** 🚀

## Quick Start

1. **Copy `fungraphics.py` to your project folder**
2. **Import and code:**

```python
from fungraphics import FunGraphics

fg = FunGraphics(800, 600, title="My App")
fg.setColor((255, 0, 0))
fg.drawFillRect(100, 100, 200, 150)

while True:
    fg.syncGameLogic(60)
```

That's it! No `sys.path.append()`, no installation needed.

## What's Included

Everything from the full package:
- ✅ All drawing methods (25+)
- ✅ Text rendering with alignment
- ✅ Image support (with optional PIL)
- ✅ Keyboard & mouse input
- ✅ Game loop with FPS control
- ✅ All constants and utilities

## Requirements

- **Python 3.7+**
- **tkinter** (included with Python)
- **Pillow** (optional, for image transformations)

## Examples

See [simple_example.py](simple_example.py) for a working demonstration.

## Documentation

Full documentation: [README.md](README.md)

---

Perfect for **students**, **quick prototypes**, and **teaching environments**!
