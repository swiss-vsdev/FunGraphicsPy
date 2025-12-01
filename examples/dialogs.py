import tkinter as tk
from tkinter import simpledialog, messagebox
import sys

class Dialogs:
    """
    This class allows to display simple messages and have graphical interfaces to
    enter words and characters.
    """

    @staticmethod
    def _get_root():
        # Try to get the existing root window, or create a hidden one if needed
        try:
            root = tk._default_root
            if root is None:
                root = tk.Tk()
                root.withdraw() # Hide the main window
            return root
        except:
            root = tk.Tk()
            root.withdraw()
            return root

    @staticmethod
    def get_hidden_string(message):
        """
        This function open a dialog box to enter a hidden String.
        :param message: The message displayed to ask for the hidden String
        :return: The hidden String entered
        """
        # Tkinter simpledialog doesn't support 'show' (masking) directly in askstring until recently or via custom dialog.
        # Actually askstring has a 'show' parameter.
        
        root = Dialogs._get_root()
        
        while True:
            s = simpledialog.askstring("Input", message, show='*', parent=root)
            if s is None:
                # User cancelled, maybe return empty or exit? Scala version doesn't handle cancel explicitly well (returns empty string maybe?)
                # Scala code: if s.length > 0 s else getHiddenString...
                # If cancel, s is None.
                return "" 
            if len(s) > 0:
                return s
            # If empty, ask again as per Scala logic
            message = "Enter at least one character"

    @staticmethod
    def get_char(message):
        """
        This function open a dialog box to enter a character.
        :param message: The message asking for the character.
        :return: The character entered.
        """
        root = Dialogs._get_root()
        
        while True:
            s = simpledialog.askstring("Input a character please", message, parent=root)
            if s is None:
                sys.exit(-1) # Match Scala behavior
            if len(s) == 1:
                return s[0]
            # Else ask again
            message = "Just one character"

    @staticmethod
    def display_message(message):
        """
        Open a dialog box to display a message.
        :param message: The message to display.
        """
        root = Dialogs._get_root()
        messagebox.showinfo("Message", message, parent=root)
