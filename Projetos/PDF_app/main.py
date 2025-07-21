import tkinter as tk
from tkinter import ttk

class PdfHandler():
    def __init__(self):
        self.filepaths = []

class App(tk.Tk):
    def __init__(self, handler):
        super().__init__()
        
        # app
        self.geometry("300x400")
        self.font = ("Helvetica", 12)

        # pdf arguments
        self.handler = handler()

        self.setup_gui()
        self.setup_styler()
    
    def setup_styler(self):
        self.styler = ttk.Style(self)
        self.styler.configure("Frame1.TFrame", background="#000000")
        self.styler.configure("Frame2.TFrame", background="#1A1A1A")
        self.styler.configure("TLabel", background="#000000", foreground="#5eeb00", font=self.font)

    def setup_gui(self):
        # definir frames
        self.mainframe = ttk.Frame(self, style="Frame1.TFrame")
        self.mainframe.pack(expand=True, fill="both")

        self.titleframe = ttk.Frame(self.mainframe, style="Frame1.TFrame")
        self.titleframe.pack(pady=5,padx=5)
        ttk.Label(self.titleframe, text="App de PDFs", font=("Helvetica", 30, "bold")).pack(side="top")

        self.inputframe = ttk.Frame(self.mainframe, style="Frame2.TFrame")
        self.inputframe.pack(pady=5,padx=5, expand=True, fill="both")




root = App(PdfHandler)
root.mainloop()