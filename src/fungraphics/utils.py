import tkinter as tk
import os

class GraphicsBitmap:
    def __init__(self, filename_or_path):
        """
        Loads an image from a file.
        """
        # Check if it's a resource path (starts with /) or a file path
        if filename_or_path.startswith("/"):
             # Assuming resources are relative to the project root or src
             # For now, let's try to find it relative to current working directory
             # removing leading /
             path = filename_or_path.lstrip("/")
        else:
            path = filename_or_path
        
        self.image = None
        try:
            self.image = tk.PhotoImage(file=path)
        except Exception as e:
            print(f"Error: Image not found or format not supported at {path}. {e}")
            # Create a placeholder or leave as None
            # Tkinter PhotoImage is hard to create programmatically without data
            # We will handle None in drawPicture

    def getWidth(self):
        if self.image:
            return self.image.width()
        return 0

    def getHeight(self):
        if self.image:
            return self.image.height()
        return 0
