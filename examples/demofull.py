import sys
import os

# Add src to path to import fungraphics
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from fungraphics.fun_graphics import FunGraphics, ALIGN_LEFT, ALIGN_CENTER, ALIGN_RIGHT, ALIGN_TOP, ALIGN_BOTTOM, MOUSE_BUTTON_LEFT

class MouseListener:
    def __init__(self, demo):
        self.demo = demo
    
    def mouseClicked(self, event):
        self.demo.last_click = (event.x, event.y, event.button)
        print(f"Mouse clicked at ({event.x}, {event.y}), button: {event.button}")

class MouseMotionListener:
    def __init__(self, demo):
        self.demo = demo
    
    def mouseMoved(self, event):
        self.demo.mouse_pos = (event.x, event.y)

class DemoFull:
    def __init__(self):
        self.fg = FunGraphics(800, 600, title="FunGraphics - Complete Feature Demo")
        self.current_demo = 0
        self.frame = 0
        self.last_click = None
        self.mouse_pos = (0, 0)
        
        # Set up mouse listeners
        self.fg.addMouseListener(MouseListener(self))
        self.fg.addMouseMotionListener(MouseMotionListener(self))
        
        self.demos = [
            ("Basic Shapes", self.demo_basic_shapes),
            ("Ovals & Polygons", self.demo_ovals_polygons),
            ("Text Rendering", self.demo_text),
            ("Fancy Text", self.demo_fancy_text),
            ("Mouse Input", self.demo_mouse),
            ("Layers", self.demo_layers),
        ]
        
    def run(self):
        while True:
            self.fg.clear((255, 255, 255))
            
            # Draw current demo
            demo_name, demo_func = self.demos[self.current_demo]
            
            # Title
            self.fg.setColor((0, 0, 0))
            self.fg.drawString(10, 10, f"Demo {self.current_demo + 1}/{len(self.demos)}: {demo_name}", font_size=24)
            self.fg.drawString(10, 40, "Click anywhere to advance to next demo", font_size=14)
            
            # Run current demo
            demo_func()
            
            # Check for click to advance
            if self.last_click and self.last_click[2] == MOUSE_BUTTON_LEFT:
                self.current_demo = (self.current_demo + 1) % len(self.demos)
                self.last_click = None
                self.frame = 0
            
            self.frame += 1
            self.fg.syncGameLogic(30)
    
    def demo_basic_shapes(self):
        """Demo basic shapes: lines, rectangles, circles."""
        y = 80
        
        # Line
        self.fg.setColor((255, 0, 0))
        self.fg.setPenWidth(3)
        self.fg.drawLine(50, y, 200, y)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(210, y - 10, "drawLine()", font_size=12)
        
        # Rectangle outline
        y += 60
        self.fg.setColor((0, 255, 0))
        self.fg.setPenWidth(2)
        self.fg.drawRect(50, y, 100, 60)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(160, y + 20, "drawRect()", font_size=12)
        
        # Filled rectangle
        y += 80
        self.fg.setColor((0, 0, 255))
        self.fg.drawFillRect(50, y, 100, 60)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(160, y + 20, "drawFillRect()", font_size=12)
        
        # Circle outline
        y += 80
        self.fg.setColor((255, 0, 255))
        self.fg.setPenWidth(2)
        self.fg.drawCircle(50, y, 60)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(120, y + 20, "drawCircle()", font_size=12)
        
        # Filled circle
        y += 80
        self.fg.setColor((255, 165, 0))
        self.fg.drawFilledCircle(50, y, 60)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(120, y + 20, "drawFilledCircle()", font_size=12)
    
    def demo_ovals_polygons(self):
        """Demo ovals and polygons."""
        # Filled oval
        self.fg.setColor((100, 200, 255))
        self.fg.drawFilledOval(50, 80, 150, 100)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(210, 120, "drawFilledOval()", font_size=12)
        
        # Triangle (polygon)
        triangle = [(100, 220), (50, 300), (150, 300)]
        self.fg.setColor((255, 100, 100))
        self.fg.drawFilledPolygon(triangle)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(170, 260, "drawFilledPolygon() - Triangle", font_size=12)
        
        # Pentagon
        import math
        cx, cy, r = 400, 200, 80
        pentagon = [(cx + r * math.cos(2 * math.pi * i / 5 - math.pi/2), 
                     cy + r * math.sin(2 * math.pi * i / 5 - math.pi/2)) 
                    for i in range(5)]
        self.fg.setColor((100, 255, 100))
        self.fg.drawFilledPolygon(pentagon)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(500, 200, "Pentagon", font_size=12)
        
        # Star (outline)
        cx, cy, r_outer, r_inner = 600, 400, 70, 30
        star = []
        for i in range(10):
            r = r_outer if i % 2 == 0 else r_inner
            angle = 2 * math.pi * i / 10 - math.pi/2
            star.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
        self.fg.setColor((255, 215, 0))
        self.fg.setPenWidth(3)
        self.fg.drawPolygon(star)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(680, 400, "Star (outline)", font_size=12)
    
    def demo_text(self):
        """Demo text rendering and alignment."""
        y = 100
        
        # Basic text
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(50, y, "Basic drawString()", font_size=20)
        
        # Get text size
        y += 50
        text = "Measured text"
        size = self.fg.getStringSize(text, 20)
        self.fg.setColor((200, 200, 200))
        self.fg.drawFillRect(50, y, size[0], size[1])
        self.fg.setColor((0, 0, 255))
        self.fg.drawString(50, y, text, font_size=20)
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(50 + size[0] + 10, y, f"Size: {size}", font_size=12)
        
        # Aligned text
        y += 80
        cx = 400
        self.fg.setColor((255, 0, 0))
        self.fg.drawLine(cx, y - 20, cx, y + 120)  # Center line
        
        self.fg.setColor((0, 0, 0))
        self.fg.drawStringAligned(cx, y, "Left Aligned", font_size=16, halign=ALIGN_LEFT, valign=ALIGN_TOP)
        self.fg.drawStringAligned(cx, y + 40, "Center Aligned", font_size=16, halign=ALIGN_CENTER, valign=ALIGN_TOP)
        self.fg.drawStringAligned(cx, y + 80, "Right Aligned", font_size=16, halign=ALIGN_RIGHT, valign=ALIGN_TOP)
    
    def demo_fancy_text(self):
        """Demo fancy text with shadows and outlines."""
        y = 120
        
        # Text with shadow
        self.fg.setColor((0, 0, 255))
        self.fg.drawFancyString(50, y, "Text with Shadow", font_size=30, shadow_offset=3)
        
        # Text with outline
        y += 80
        self.fg.setColor((255, 0, 0))
        self.fg.drawFancyString(50, y, "Text with Outline", font_size=30, shadow_offset=0, outline_thickness=2)
        
        # Text with both
        y += 80
        self.fg.setColor((0, 200, 0))
        self.fg.drawFancyString(50, y, "Shadow + Outline", font_size=30, shadow_offset=3, outline_thickness=1)
        
        # Animated fancy text
        y += 100
        offset = int(5 * abs(math.sin(self.frame * 0.1)))
        self.fg.setColor((255, 165, 0))
        self.fg.drawFancyString(50, y, "Animated Shadow!", font_size=35, shadow_offset=offset, outline_thickness=1)
    
    def demo_mouse(self):
        """Demo mouse input."""
        import math
        
        # Show mouse position
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(50, 100, f"Mouse Position: {self.mouse_pos}", font_size=16)
        
        # Draw crosshair at mouse position
        mx, my = self.mouse_pos
        self.fg.setColor((255, 0, 0))
        self.fg.drawLine(mx - 10, my, mx + 10, my)
        self.fg.drawLine(mx, my - 10, mx, my + 10)
        
        # Show last click
        if self.last_click:
            cx, cy, button = self.last_click
            self.fg.drawString(50, 130, f"Last Click: ({cx}, {cy}), Button: {button}", font_size=16)
            
            # Draw circle at last click position
            self.fg.setColor((0, 255, 0))
            self.fg.drawFilledCircle(cx - 15, cy - 15, 30)
        
        # Interactive: draw circles that follow mouse
        self.fg.setColor((100, 100, 255))
        for i in range(5):
            delay = i * 5
            if self.frame > delay:
                # Lag behind mouse position
                lag_factor = 0.1 * (i + 1)
                lx = int(mx * lag_factor + 400 * (1 - lag_factor))
                ly = int(my * lag_factor + 300 * (1 - lag_factor))
                self.fg.drawFilledCircle(lx - 10, ly - 10, 20)
    
    def demo_layers(self):
        """Demo dual layer graphics."""
        # Draw on background layer
        self.fg.drawBackground()
        self.fg.setColor((200, 200, 255))
        self.fg.drawFillRect(0, 0, 800, 600)
        
        # Draw grid on background
        self.fg.setColor((180, 180, 220))
        for x in range(0, 800, 50):
            self.fg.drawLine(x, 0, x, 600)
        for y in range(0, 600, 50):
            self.fg.drawLine(0, y, 800, y)
        
        # Switch to foreground
        self.fg.drawForeground()
        
        # Draw animated shapes on foreground
        import math
        cx, cy = 400, 300
        r = 100 + 50 * math.sin(self.frame * 0.05)
        
        self.fg.setColor((255, 100, 100))
        self.fg.drawFilledCircle(int(cx - r/2), int(cy - r/2), int(r))
        
        self.fg.setColor((0, 0, 0))
        self.fg.drawString(50, 100, "Background: Static grid", font_size=16)
        self.fg.drawString(50, 130, "Foreground: Animated circle", font_size=16)
        self.fg.drawString(50, 160, "(Layers allow separation of static/dynamic content)", font_size=12)

if __name__ == "__main__":
    import math  # Import at module level for demos
    DemoFull().run()
