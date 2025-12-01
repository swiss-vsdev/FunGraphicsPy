import sys
import os

# Add src to path to import fungraphics
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from fungraphics.fun_graphics import FunGraphics, K_s, K_LEFT, K_RIGHT

class KeyAdapter:
    def __init__(self, demo):
        self.demo = demo

    def keyPressed(self, event):
        if event.key == K_s:
            print("Saving file... (Not implemented yet)")
            # self.demo.fg.saveAsPNG("fungraphics_screenshot")
        if event.key == K_LEFT:
            self.demo.pressedUp = True
        if event.key == K_RIGHT:
            self.demo.pressedDown = True

    def keyReleased(self, event):
        if event.key == K_LEFT:
            self.demo.pressedUp = False
        if event.key == K_RIGHT:
            self.demo.pressedDown = False

class Demo:
    def __init__(self):
        self.fg = FunGraphics(500, 500, "Checking basic capabilities")
        self.pressedUp = False
        self.pressedDown = False
        self.size = 1
        
    def run(self):
        self.fg.setPixel(10, 10)
        
        i = 1
        direction = 1
        
        # Colors
        yellow = (255, 255, 0)
        
        self.fg.setKeyManager(KeyAdapter(self))
        
        while True:
            if self.pressedUp:
                self.size += 1
            if self.pressedDown:
                self.size = 0 if self.size == 0 else self.size - 1
                
            self.fg.clear((255, 255, 255)) # White
            
            self.fg.setColor((255, 0, 0)) # Red
            self.fg.drawFilledCircle(50, 50, 100 + self.size)
            
            self.fg.setColor((0, 0, 0))
            self.fg.drawString(50, 250, "FunGraphics Python")
            
            # Draw rect (transparency removed in Tkinter port for simplicity)
            self.fg.setColor(yellow)
            self.fg.drawFillRect(50 + i, 50 + i, 100 + i, 100 + i)
            
            self.fg.setColor((0, 0, 255)) # Blue
            self.fg.drawLine(100, 100, 150, 150)
            
            i += direction
            if i > 100 or i <= 0:
                direction *= -1
                
            self.fg.syncGameLogic(60)

if __name__ == "__main__":
    Demo().run()
