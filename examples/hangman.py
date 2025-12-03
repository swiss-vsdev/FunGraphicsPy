import sys
import os
import time

# Add src to path to import fungraphics
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from fungraphics import FunGraphics
from dialogs import Dialogs

class WordManager:
    def __init__(self):
        self.secret_word = ""
        self.user_word = ""

    def ask_secret_word(self):
        # Dialogs.get_hidden_string returns a string
        self.secret_word = Dialogs.get_hidden_string("Insert secret word").lower()
        self.user_word = "*" * len(self.secret_word)

    def check_letter(self, c):
        c = c.lower()
        is_part = False
        temp_word = list(self.user_word)
        
        for i, char in enumerate(self.secret_word):
            if char == c:
                temp_word[i] = c
                is_part = True
        
        self.user_word = "".join(temp_word)
        return is_part

    def is_word_complete(self):
        return "*" not in self.user_word

class HangMan:
    def __init__(self):
        self.MAX_STEPS = 8
        self.current_step = 0
        self.window_width = 300
        self.window_height = 300
        self.display = FunGraphics(self.window_width, self.window_height, title="HangMan")
        self.wm = WordManager()
        self.running = False

    def update_graphics_view(self):
        step = self.current_step
        self.display.setColor((0, 0, 0)) # Black
        
        # Draw stickman parts based on current step
        if step == 1:
            self.display.drawLine(110, 210, 120, 190)
            self.display.drawLine(130, 210, 120, 190)
        elif step == 2:
            self.display.drawLine(120, 190, 120, 100)
        elif step == 3:
            self.display.drawLine(120, 100, 180, 100)
        elif step == 4:
            self.display.drawLine(180, 100, 180, 110)
        elif step == 5:
            self.display.drawCircle(170, 110, 20)
        elif step == 6:
            self.display.drawLine(180, 130, 180, 170)
        elif step == 7:
            self.display.drawLine(170, 190, 180, 170)
            self.display.drawLine(180, 170, 190, 190)
        elif step == 8:
            self.display.drawLine(170, 150, 190, 150)
            
        # Clear text area (top 100 pixels to be safe)
        self.display.setColor((255, 255, 255)) # White
        self.display.drawFillRect(0, 0, 300, 100)
        
        # Draw text
        self.display.setColor((0, 0, 0)) # Black
        # Move text up slightly to fit better in cleared area
        self.display.drawString(20, 40, f"Word : {self.wm.user_word}")
        
        if self.running:
             result_text = "LOSER" if self.current_step == self.MAX_STEPS else "YOU WON !"
             self.display.drawString(20, 260, f"Result : {result_text}")
             
        # Force update
        self.display.syncGameLogic(60)

    def play(self):
        while True:
            game_status = True
            self.current_step = 0
            self.display.clear((255, 255, 255))
            self.wm.ask_secret_word()
            print("Okaaaaaaaay, let's goooooo !")
            
            # Initial view
            self.update_graphics_view()
            
            while self.current_step < self.MAX_STEPS and game_status:
                # Get input
                char_input = Dialogs.get_char("Enter a letter").lower()
                
                if self.wm.check_letter(char_input):
                    if self.wm.is_word_complete():
                        print(f"Congratulations !\nThe word was {self.wm.user_word}\nYou failed {self.current_step} {'time' if self.current_step < 2 else 'times'}")
                        game_status = False
                    else:
                        print(f"Good Job !\n{self.wm.user_word}")
                else:
                    if self.current_step < self.MAX_STEPS:
                        self.current_step += 1
                        print(f"Try Again !\n{self.wm.user_word}")
                        print(self.current_step)
                
                self.update_graphics_view()
            
            if self.current_step == self.MAX_STEPS:
                print("LOSER")
                game_status = False
                
            self.running = True
            self.update_graphics_view()
            self.running = False
            
            # Play again?
            again = Dialogs.get_char("Want to play again ? (Y for yes)")
            if again.lower() != 'y':
                sys.exit(0)

if __name__ == "__main__":
    HangMan().play()
