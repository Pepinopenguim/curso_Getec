import tkinter as tk
from tkinter import ttk, filedialog

class PdfHandler():
    def __init__(self):
        self.filepaths = []

class App(tk.Tk):
    def __init__(self, handler):
        super().__init__()
        
        # app
        self.geometry("400x400")
        self.minsize(400, 400)
        self.font = ("Consolas", 12)

        # pdf arguments
        self.handler = handler()

        self.setup_gui()
        self.setup_styler()
        self.setup_inputs()
    
    def setup_styler(self):
        self.styler = ttk.Style(self)
        # Stilo 1
        self.styler.configure("style1.TFrame", background="#000000")
        self.styler.configure("style1.TLabel", background="#000000", foreground="#5eeb00", font=self.font)

        # Stilo 2
        self.styler.configure("style2.TFrame", background="#1A1A1A")
        self.styler.configure("style2.TLabel", background="#1A1A1A", foreground="#5eeb00", font=self.font)

    def TButton2(self, *args, **kwargs):
        return tk.Button(*args, **kwargs, font=self.font, background="#1A1A1A", foreground="#5eeb00", width=12)

    def setup_gui(self):
        # definir frames
        self.mainframe = ttk.Frame(self, style="style1.TFrame")
        self.mainframe.pack(expand=True, fill="both")

        self.titleframe = ttk.Frame(self.mainframe, style="style1.TFrame")
        self.titleframe.pack(pady=5,padx=5)
        ttk.Label(self.titleframe, text="App de PDFs", font=(self.font[0], 30, "bold"), style="style1.TLabel").pack(side="top")

        self.inputframe = ttk.Frame(self.mainframe, style="style2.TFrame")
        self.inputframe.pack(pady=5,padx=5, expand=True, fill="both")
    
    def setup_inputs(self):
        # ============ Linha 1 ============
        line1 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line1.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line1, text="Escolher Arquivos PDF:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.TButton2(line1, text="Procurar", command=self.get_files).pack(side="right", padx=5, anchor="e")

        self.num_files_label = ttk.Label(line1, text="0", style="style2.TLabel")
        self.num_files_label.pack(side="right", padx=(0,5), anchor="e")

        # ============ Linha 2 ============
        line2 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line2.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line2, text="Unir arquivos em um:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.TButton2(line2, text="Unir", command=self.get_files).pack(side="right", padx=5, anchor="e")


    def get_files(self):
        filetypes = (
            ("Pdf files", ".pdf"),
            ("All files", "*.*")
        )

        files = filedialog.askopenfilenames(filetypes=filetypes)

        self.handler.filepaths = list(files)

        self.num_files_label.config(text=str(len(self.handler.filepaths)))
        
        




root = App(PdfHandler)
root.mainloop()