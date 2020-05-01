"""
Program: filedialogdemo.py
Author: Andrew
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
    """Demonstrates the use of a file dialog."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "File Dialog Demo")
        self.outputArea = self.addTextArea(text = "", row = 0, column = 0, width = 80, height = 25)
        self.addButton(text = "Open", row = 1, column = 0, command = self.openFile)

    # Event handling method.
    def openFile(self):
        """Pops up an open file dialog, and if a file is selected, display it's text in the text area and it's pathname in the title bar."""
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]

        fileName = tkinter.filedialog.askopenfilename(parent = self, filetype = fList)

        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)

# Definition of the main() function
def main():
    FileDialogDemo().mainloop()

main()