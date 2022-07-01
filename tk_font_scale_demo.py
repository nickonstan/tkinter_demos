"""
Demo showcasing a solution for dynamically resized text using tkinter.
The text will adapt its size to match its parent widget when the window
containing it is shrunk.

Author: Nick Konstantinidis
Date created: 01-July-22
Date last modified: 01-July-22
Python version: 3.9
"""

import tkinter as tk
from tkinter import font


class Gui(tk.Frame):
    def __init__(self, parent=None):
        """
        GUI Constructor
        """
        tk.Frame.__init__(self, parent)
        self.font = font.Font(family="Arial", size=-48, weight="bold")
        self.label = tk.Label(self, text="Shrink the window", font=self.font, fg="white", bg="black")
        self.label.pack(expand=tk.YES, fill=tk.BOTH)
        """
        The function "fit_text_to_frame" is called every time the main window
        is resized.
        """
        self.label.bind('<Configure>', lambda e, parent=self, label=self.label, font=self.font:
                        self.fit_text_to_frame(parent, label, font))

    def text_width(self, label, font) -> int:
        """
        Returns the width (in pixels) of the text of a label

        Parameters
        ----------
        label : tkinter.Label widget
        font  : tkinter.font.Font object
        """
        return font.measure(label.cget('text'))

    def wider_than_parent(self, parent, label, font) -> bool:
        """
        Checks if the text of a label is wider than its parent widget.

        Parameters
        ----------
        parent : tkinter widget
        label : tkinter.Label widget
        font  : tkinter.font.Font object
        """
        self.update_idletasks()
        if self.text_width(label, font) > parent.winfo_width():
            return True
        else:
            return False

    def decrease_font_size(self, font, pixels=1, limit=-12) -> None:
        """
        Decreases the size (height) of a font by a certain amount of pixels.
        The size value should be negative when referring to pixels.
        The font will not get smaller when it reaches a specified limit.
        """
        if font.cget('size') < limit:
            font.configure(size=font.cget('size')+pixels)
        else:
            pass

    def fit_text_to_frame(self, parent, label, font) -> None:
        """
        Decreases the size of a font until it fits in its parent widget.
        """
        while self.wider_than_parent(parent, label, font):
            self.decrease_font_size(font)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Font Scaling Demo")
    root.geometry("500x200")
    Gui(root).pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()
