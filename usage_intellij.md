# Use in IntelliJ IDEA

## Prerequisites

*   **IntelliJ IDEA**: Ensure you have the [Python plugin](https://plugins.jetbrains.com/plugin/631-python) installed (it comes bundled with IntelliJ IDEA Ultimate, but needs to be installed for Community Edition).
*   **Python**: Make sure Python 3.x is installed on your system.

## Setting up the Project

1.  **Open the Project**:
    *   Launch IntelliJ IDEA.
    *   Click `Open` or `File > Open...`.
    *   Select the `FunGraphics` folder (the root of this repository).

2.  **Configure the Python Interpreter**:
    *   If IntelliJ detects a Python file, it might prompt you to configure an SDK.
    *   Go to `File > Project Structure...` (or `Cmd + ;` on macOS).
    *   Under `Platform Settings` > `SDKs`, ensure a Python SDK is added. If not, click `+` > `Add Python SDK...` and select your system interpreter or create a virtual environment.
    *   Under `Project Settings` > `Project`, select the Python SDK you just added as the **Project SDK**.

3.  **Mark Source Directory** (Optional but Recommended):
    *   In the **Project** view (left panel), right-click on the `src` folder.
    *   Select `Mark Directory as` > `Sources Root`.
    *   *This tells IntelliJ that your library code lives here, helping with auto-completion and imports.*

## Running Examples

1.  Open `examples/demo.py` or `examples/hangman.py`.
2.  Right-click anywhere in the editor.
3.  Select `Run 'demo'` (or `Run 'hangman'`).

## Testing Installation

You can create a new Python file in the project root (e.g., `test_setup.py`) with the following code to verify everything is working:

```python
import sys
import os

# Ensure src is in the path if you haven't marked it as Sources Root
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fungraphics import FunGraphics

def main():
    fg = FunGraphics(400, 300, title="IntelliJ Setup Test")
    fg.setColor((0, 200, 0))
    fg.drawString(50, 150, "It works!", font_size=30)
    
    # Keep window open
    while True:
        fg.syncGameLogic(60)

if __name__ == "__main__":
    main()
```

**Note**: If you marked `src` as Sources Root in step 3, you can use even simpler imports:
```python
from fungraphics import FunGraphics
```
