import tkinter as tk
from tkinter import scrolledtext

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input = tk.Entry(self)
        self.input.pack(side="top")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Convert to Text"
        self.hi_there["command"] = self.convert_to_text
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="bottom")

        self.text_area = scrolledtext.ScrolledText(self, width=40, height=10)
        self.text_area.pack(side='bottom')

    def convert_to_text(self):
        text = self.input.get()
        self.text_area.insert(tk.INSERT, text + '\n')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
