# 🎨 FunGraphics for Python 🐍

Welcome to **FunGraphics**, a Python port of the library originally designed for teaching imperative programming at [HES-SO Valais//Wallis](https://www.hevs.ch).

This library makes 2D graphics **fun** and **easy**! It's perfect for learning how to code games, visualizations, and interactive apps without getting bogged down in complex frameworks.

---

## ✨ Features

- 🖌️ **Simple 2D Graphics**: Draw lines, rectangles, circles, text, and images with simple commands.
- ⌨️ **Input Handling**: React to keyboard events instantly.
- 💬 **Dialogs**: Built-in popups for asking questions (strings, characters) and showing messages.
- 🚀 **Native Backend**: Built on `tkinter` (standard Python). No heavy downloads or complex setups!

---

## 🛠️ Requirements

- 🐍 **Python 3.x**
- 🖼️ **Tkinter**: Usually comes pre-installed with Python.
    - *🍎 macOS users*: If you see an error, just run:
      ```bash
      brew install python-tk
      ```

## 💻 IDE Setup

- [IntelliJ IDEA Setup Guide](usage_intellij.md)

---

## 🚀 Getting Started

Clone the repository and you are ready to code! The library is self-contained in the `src` directory.

### 🎮 Running Examples

We've included some cool examples to get you started:

**🔹 Basic Demo**
See what the library can do:
```bash
python3 examples/demo.py
```

**😵 Hangman Game**
A fully playable game:
```bash
python3 examples/hangman.py
```

---

## 👩‍💻 Creating Your Own App

It's super easy to start your own project. Here is a template:

1.  Create a new file (e.g., `my_game.py`).
2.  Make sure the `src` folder is nearby.
3.  Copy-paste this code:

```python
import sys
import os
# 🔌 Connect to the library
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fungraphics.fun_graphics import FunGraphics

def main():
    # 1️⃣ Create a window
    fg = FunGraphics(800, 600, "My Awesome App 🚀")
    
    # 2️⃣ Draw something cool
    fg.setColor((255, 0, 0)) # 🔴 Red
    fg.drawFillRect(100, 100, 200, 150)
    
    fg.setColor((0, 0, 255)) # 🔵 Blue
    fg.drawString(100, 300, "Hello World!", font_size=40)
    
    # 3️⃣ Keep it running
    while True:
        fg.syncGameLogic(60) # 60 FPS

if __name__ == "__main__":
    main()
```

---

## 📂 Project Structure

Here's where everything lives:

- 📦 **`src/fungraphics/`**: The magic happens here (Library code).
    - `fun_graphics.py`: The main graphics engine.
    - `utils.py`: Helpers for images.
- 💡 **`examples/`**: Learn by example.
    - `hangman.py`: The classic word game.
    - `demo.py`: Shows off all the drawing features.
    - `dialogs.py`: Helpers for popups.

---

## 📜 Origin

Based on the original [FunGraphics](https://github.com/isc-hei/FunGraphics) library for Scala/Java developed by P.-A. Mudry. Ported with ❤️ to Python.
