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

# Text alignment constants
ALIGN_LEFT = 'left'
ALIGN_CENTER = 'center'
ALIGN_RIGHT = 'right'
ALIGN_TOP = 'top'
ALIGN_BOTTOM = 'bottom'

# Mouse button constants
MOUSE_BUTTON_LEFT = 1
MOUSE_BUTTON_MIDDLE = 2
MOUSE_BUTTON_RIGHT = 3

class FunGraphics:
    def __init__(self, width, height, xoffset=-1, yoffset=-1, title="FunGraphics", high_quality=True):
        self.width = width
        self.height = height
        self.title = title
        
        self.root = tk.Tk()
        self.root.title(title)
        
        # Set window position if specified
        if xoffset >= 0 and yoffset >= 0:
            self.root.geometry(f"{width}x{height}+{xoffset}+{yoffset}")
        else:
            self.root.geometry(f"{width}x{height}")
        
        self.root.resizable(False, False)
        
        # Create dual layers for background and foreground
        self.canvas = tk.Canvas(self.root, width=width, height=height, highlightthickness=0)
        self.canvas.pack()
        
        # Store layer state
        self.current_layer = 'foreground'
        self.background_items = []
        self.foreground_items = []
        
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
        self.mouse_listeners = []
        self.mouse_motion_listeners = []
        
        self.root.bind("<KeyPress>", self._on_key_press)
        self.root.bind("<KeyRelease>", self._on_key_release)
        self.canvas.bind("<Button>", self._on_mouse_click)
        self.canvas.bind("<Motion>", self._on_mouse_motion)
        
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
        if self.window_closed:
            return
        c = self.color if color is None else self._rgb_to_hex(color)
        # Draw a 1x1 rectangle (line might be invisible if length 0)
        self.canvas.create_rectangle(x, y, x+1, y+1, fill=c, outline="")
        
    def setPenWidth(self, width):
        self.line_width = int(width)
        
    def drawLine(self, x1, y1, x2, y2):
        if self.window_closed:
            return
        self.canvas.create_line(x1, y1, x2, y2, fill=self.color, width=self.line_width)
        
    def drawRect(self, x, y, width, height):
        if self.window_closed:
            return
        self.canvas.create_rectangle(x, y, x+width, y+height, outline=self.color, width=self.line_width)
        
    def drawFillRect(self, x, y, width, height):
        if self.window_closed:
            return
        self.canvas.create_rectangle(x, y, x+width, y+height, fill=self.color, outline="")
        
    def drawCircle(self, x, y, diameter):
        if self.window_closed:
            return
        self.canvas.create_oval(x, y, x+diameter, y+diameter, outline=self.color, width=self.line_width)
        
    def drawFilledCircle(self, x, y, diameter):
        if self.window_closed:
            return
        self.canvas.create_oval(x, y, x+diameter, y+diameter, fill=self.color, outline="")
        
    def drawString(self, x, y, text, font_size=20, color=None):
        if self.window_closed:
            return
        c = self.color if color is None else self._rgb_to_hex(color)
        font = (self.font_name, font_size)
        self.canvas.create_text(x, y, text=text, fill=c, font=font, anchor="nw")
        
    def drawPicture(self, x, y, bitmap):
        if self.window_closed:
            return
        # Centered drawing
        if bitmap.image:
            self.canvas.create_image(x, y, image=bitmap.image, anchor="c")
    
    def drawFilledOval(self, x, y, width, height):
        """Draw a filled oval (ellipse)."""
        if self.window_closed:
            return
        self.canvas.create_oval(x, y, x+width, y+height, fill=self.color, outline="")
    
    def drawPolygon(self, points):
        """Draw a polygon outline from a list of (x, y) tuples."""
        if self.window_closed:
            return
        if len(points) < 3:
            return
        flat_points = [coord for point in points for coord in point]
        self.canvas.create_polygon(flat_points, outline=self.color, fill="", width=self.line_width)
    
    def drawFilledPolygon(self, points, color=None):
        """Draw a filled polygon from a list of (x, y) tuples."""
        if self.window_closed:
            return
        if len(points) < 3:
            return
        c = self.color if color is None else self._rgb_to_hex(color)
        flat_points = [coord for point in points for coord in point]
        self.canvas.create_polygon(flat_points, fill=c, outline=c)
    
    def getStringSize(self, text, font_size=None):
        """
        Get the dimensions of a text string.
        Returns a tuple (width, height).
        """
        if font_size is None:
            font_size = self.font_size
        font = (self.font_name, font_size)
        # Create a temporary text item to measure
        temp_id = self.canvas.create_text(0, 0, text=text, font=font, anchor="nw")
        bbox = self.canvas.bbox(temp_id)
        self.canvas.delete(temp_id)
        if bbox:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            return (width, height)
        return (0, 0)
    
    def drawStringAligned(self, x, y, text, font_size=20, color=None, halign=ALIGN_LEFT, valign=ALIGN_BOTTOM):
        """
        Draw text with horizontal and vertical alignment.
        halign: ALIGN_LEFT, ALIGN_CENTER, ALIGN_RIGHT
        valign: ALIGN_TOP, ALIGN_CENTER, ALIGN_BOTTOM
        """
        if self.window_closed:
            return
        c = self.color if color is None else self._rgb_to_hex(color)
        font = (self.font_name, font_size)
        
        # Map alignment to tkinter anchor
        anchor_map = {
            (ALIGN_LEFT, ALIGN_TOP): "nw",
            (ALIGN_LEFT, ALIGN_CENTER): "w",
            (ALIGN_LEFT, ALIGN_BOTTOM): "sw",
            (ALIGN_CENTER, ALIGN_TOP): "n",
            (ALIGN_CENTER, ALIGN_CENTER): "center",
            (ALIGN_CENTER, ALIGN_BOTTOM): "s",
            (ALIGN_RIGHT, ALIGN_TOP): "ne",
            (ALIGN_RIGHT, ALIGN_CENTER): "e",
            (ALIGN_RIGHT, ALIGN_BOTTOM): "se",
        }
        
        anchor = anchor_map.get((halign, valign), "nw")
        self.canvas.create_text(x, y, text=text, fill=c, font=font, anchor=anchor)
    
    def drawFancyString(self, x, y, text, font_size=20, color=None, shadow_offset=2, outline_thickness=0):
        """
        Draw text with shadow and/or outline effects.
        shadow_offset: pixels to offset shadow (0 for no shadow)
        outline_thickness: thickness of outline (0 for no outline)
        """
        if self.window_closed:
            return
        c = self.color if color is None else self._rgb_to_hex(color)
        font = (self.font_name, font_size)
        
        # Draw outline
        if outline_thickness > 0:
            outline_color = "#FFFFFF"  # White outline
            for dx in range(-outline_thickness, outline_thickness + 1):
                for dy in range(-outline_thickness, outline_thickness + 1):
                    if dx != 0 or dy != 0:
                        self.canvas.create_text(x + dx, y + dy, text=text, fill=outline_color, font=font, anchor="nw")
        
        # Draw shadow
        if shadow_offset > 0:
            shadow_color = "#808080"  # Gray shadow
            self.canvas.create_text(x + shadow_offset, y + shadow_offset, text=text, fill=shadow_color, font=font, anchor="nw")
        
        # Draw main text
        self.canvas.create_text(x, y, text=text, fill=c, font=font, anchor="nw")
    
    def drawTransformedPicture(self, x, y, bitmap, angle=0, scale=1.0):
        """
        Draw an image with rotation and scaling.
        angle: rotation angle in degrees
        scale: scaling factor (1.0 = original size)
        """
        if self.window_closed:
            return
        if not bitmap.image:
            return
        
        # Note: tkinter doesn't support image rotation/scaling directly
        # This is a simplified version - full implementation would require PIL
        try:
            from PIL import Image, ImageTk
            import math
            
            # Get the original PIL image
            pil_image = bitmap.pil_image if hasattr(bitmap, 'pil_image') else None
            if pil_image is None:
                # Fallback: just draw normally
                self.drawPicture(x, y, bitmap)
                return
            
            # Apply transformations
            if scale != 1.0:
                new_width = int(pil_image.width * scale)
                new_height = int(pil_image.height * scale)
                pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            if angle != 0:
                pil_image = pil_image.rotate(-angle, expand=True)  # Negative for clockwise
            
            # Convert back to PhotoImage
            photo = ImageTk.PhotoImage(pil_image)
            # Store reference to prevent garbage collection
            if not hasattr(self, '_image_refs'):
                self._image_refs = []
            self._image_refs.append(photo)
            
            self.canvas.create_image(x, y, image=photo, anchor="c")
        except ImportError:
            # PIL not available, just draw normally
            self.drawPicture(x, y, bitmap)
    
    def drawMirroredPicture(self, x, y, bitmap, horizontal=True):
        """
        Draw a mirrored (flipped) image.
        horizontal: if True, flip horizontally; if False, flip vertically
        """
        if self.window_closed:
            return
        if not bitmap.image:
            return
        
        try:
            from PIL import Image, ImageTk, ImageOps
            
            pil_image = bitmap.pil_image if hasattr(bitmap, 'pil_image') else None
            if pil_image is None:
                self.drawPicture(x, y, bitmap)
                return
            
            # Mirror the image
            if horizontal:
                pil_image = ImageOps.mirror(pil_image)
            else:
                pil_image = ImageOps.flip(pil_image)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(pil_image)
            if not hasattr(self, '_image_refs'):
                self._image_refs = []
            self._image_refs.append(photo)
            
            self.canvas.create_image(x, y, image=photo, anchor="c")
        except ImportError:
            self.drawPicture(x, y, bitmap)
    
    def saveAsPNG(self, filename):
        """
        Save the current canvas as a PNG image.
        Requires PIL/Pillow.
        """
        try:
            from PIL import Image, ImageGrab
            import platform
            
            # Get canvas position
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            
            # Grab the canvas area
            if platform.system() == "Darwin":  # macOS
                # On macOS, we need to use a different approach
                self.canvas.postscript(file=filename + ".ps")
                print(f"Saved as PostScript: {filename}.ps (PNG export requires additional setup on macOS)")
            else:
                img = ImageGrab.grab(bbox=(x, y, x1, y1))
                if not filename.endswith('.png'):
                    filename += '.png'
                img.save(filename)
                print(f"Saved screenshot: {filename}")
        except Exception as e:
            print(f"Failed to save image: {e}")
    
    # Layer management
    def drawBackground(self):
        """Switch to drawing on the background layer."""
        self.current_layer = 'background'
    
    def drawForeground(self):
        """Switch to drawing on the foreground layer."""
        self.current_layer = 'foreground'

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
    
    def addMouseListener(self, listener):
        """
        Add a mouse listener object that has mouseClicked method.
        """
        self.mouse_listeners.append(listener)
    
    def addMouseMotionListener(self, listener):
        """
        Add a mouse motion listener object that has mouseMoved method.
        """
        self.mouse_motion_listeners.append(listener)
    
    def _on_mouse_click(self, event):
        class MockEvent:
            def __init__(self, x, y, button):
                self.x = x
                self.y = y
                self.button = button
        
        mock_event = MockEvent(event.x, event.y, event.num)
        for listener in self.mouse_listeners:
            if hasattr(listener, 'mouseClicked'):
                listener.mouseClicked(mock_event)
    
    def _on_mouse_motion(self, event):
        class MockEvent:
            def __init__(self, x, y):
                self.x = x
                self.y = y
        
        mock_event = MockEvent(event.x, event.y)
        for listener in self.mouse_motion_listeners:
            if hasattr(listener, 'mouseMoved'):
                listener.mouseMoved(mock_event)
    
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

