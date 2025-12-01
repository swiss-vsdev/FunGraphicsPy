import tkinter as tk
import time
from .utils import GraphicsBitmap

# Key constants
K_s = 's'
K_LEFT = 'Left'
K_RIGHT = 'Right'
K_UP = 'Up'
K_DOWN = 'Down'
K_SPACE = 'space'

class FunGraphics:
    def __init__(self, width, height, title="FunGraphics", high_quality=True):
        self.width = width
        self.height = height
        self.title = title
        
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(self.root, width=width, height=height, highlightthickness=0)
        self.canvas.pack()
        
        # Default settings
        self.color = "#000000" # Black
        self.line_width = 1
        self.font_name = "Arial"
        self.font_size = 20
        
        # Window state
        self.window_closed = False
        self.root.protocol("WM_DELETE_WINDOW", self._on_window_close)
        
        # Input handling
        self.key_listeners = []
        self.root.bind("<KeyPress>", self._on_key_press)
        self.root.bind("<KeyRelease>", self._on_key_release)
        
        # Clear screen initially
        self.clear((255, 255, 255)) # White
        
        self.last_time = time.time()
        
    def _rgb_to_hex(self, color):
        # Handle 3 or 4 tuple (ignore alpha for hex)
        if len(color) >= 3:
            return "#%02x%02x%02x" % (color[0], color[1], color[2])
        return "#000000"
        
    def clear(self, color=(255, 255, 255)):
        if self.window_closed:
            return
        self.canvas.delete("all")
        self.canvas.configure(bg=self._rgb_to_hex(color))
        
    def setColor(self, color):
        """
        Set the current drawing color.
        Color can be a tuple (r, g, b) or (r, g, b, a).
        """
        self.color = self._rgb_to_hex(color)
        
    def setPixel(self, x, y, color=None):
        c = self.color if color is None else self._rgb_to_hex(color)
        # Draw a 1x1 rectangle (line might be invisible if length 0)
        self.canvas.create_rectangle(x, y, x+1, y+1, fill=c, outline="")
        
    def setPenWidth(self, width):
        self.line_width = int(width)
        
    def drawLine(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill=self.color, width=self.line_width)
        
    def drawRect(self, x, y, width, height):
        self.canvas.create_rectangle(x, y, x+width, y+height, outline=self.color, width=self.line_width)
        
    def drawFillRect(self, x, y, width, height):
        self.canvas.create_rectangle(x, y, x+width, y+height, fill=self.color, outline="")
        
    def drawCircle(self, x, y, diameter):
        self.canvas.create_oval(x, y, x+diameter, y+diameter, outline=self.color, width=self.line_width)
        
    def drawFilledCircle(self, x, y, diameter):
        self.canvas.create_oval(x, y, x+diameter, y+diameter, fill=self.color, outline="")
        
    def drawString(self, x, y, text, font_size=20, color=None):
        c = self.color if color is None else self._rgb_to_hex(color)
        font = (self.font_name, font_size)
        self.canvas.create_text(x, y, text=text, fill=c, font=font, anchor="nw")
        
    def drawPicture(self, x, y, bitmap):
        # Centered drawing
        if bitmap.image:
            self.canvas.create_image(x, y, image=bitmap.image, anchor="c")

    # Input handling
    def setKeyManager(self, listener):
        """
        Register a listener object that has keyPressed and keyReleased methods.
        """
        self.key_listeners.append(listener)
        
    def _on_key_press(self, event):
        class MockEvent:
            def __init__(self, key):
                self.key = key
        
        mock_event = MockEvent(event.keysym)
        for listener in self.key_listeners:
            if hasattr(listener, 'keyPressed'):
                listener.keyPressed(mock_event)

    def _on_key_release(self, event):
        class MockEvent:
            def __init__(self, key):
                self.key = key
        
        mock_event = MockEvent(event.keysym)
        for listener in self.key_listeners:
            if hasattr(listener, 'keyReleased'):
                listener.keyReleased(mock_event)
    
    def _on_window_close(self):
        """Handle window close event."""
        self.window_closed = True
        self.root.destroy()
        import sys
        sys.exit(0)
        
    def syncGameLogic(self, fps):
        """
        Process events and update display.
        Should be called in the game loop.
        """
        if self.window_closed:
            import sys
            sys.exit(0)
        
        try:
            self.root.update_idletasks()
            self.root.update()
        except tk.TclError:
            # Window closed
            self.window_closed = True
            import sys
            sys.exit(0)
        
        # Sleep to maintain FPS
        current_time = time.time()
        elapsed = current_time - self.last_time
        target_frame_time = 1.0 / fps
        if elapsed < target_frame_time:
            time.sleep(target_frame_time - elapsed)
        self.last_time = time.time()

