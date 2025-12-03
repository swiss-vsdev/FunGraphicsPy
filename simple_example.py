"""
Simple example using the single-file fungraphics.py library.
Just place fungraphics.py in the same directory as your script!
"""

from fungraphics import FunGraphics

def main():
    # Create a window - that's it! No path manipulation needed!
    fg = FunGraphics(800, 600, title="My Awesome App 🚀")
    
    # Draw a red rectangle
    fg.setColor((255, 0, 0))
    fg.drawFillRect(100, 100, 200, 150)
    
    # Draw blue text
    fg.setColor((0, 0, 255))
    fg.drawString(100, 300, "Hello World!", font_size=40)
    
    # Draw a green circle
    fg.setColor((0, 255, 0))
    fg.drawFilledCircle(500, 200, 100)
    
    # Game loop
    while True:
        fg.syncGameLogic(60)  # 60 FPS

if __name__ == "__main__":
    main()
