import tkinter as tk
from tkinter import filedialog

class TextEditor:
    """This class represents a simple text editor"""

    def __init__(self, root):
        """Constructor method"""

        self.root = root
        self.filename = None
        self.text = tk.Text(self.root)
        self.text.pack()

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def new_file(self):
        """Create a new file"""

        self.text.delete("1.0", tk.END)
        self.filename = None

    def open_file(self):
        """Open an existing file"""

        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"),
                                                              ("All Files", "*.*")])
        if self.filename:
            self.text.delete("1.0", tk.END)
            with open(self.filename, "r") as file:
                self.text.insert(tk.END, file.read())

    def save_file(self):
        """Save the current file"""

        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text.get("1.0", tk.END))
        else:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                         filetypes=[("Text Files", "*.txt"),
                                                                    ("All Files", "*.*")])
            if self.filename:
                with open(self.filename, "w") as file:
                    file.write(self.text.get("1.0", tk.END))

# Create the main window and text editor
root = tk.Tk()
root.title("Text Editor")
editor = TextEditor(root)

# Start the main event loop
root.mainloop()
