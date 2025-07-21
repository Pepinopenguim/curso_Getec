import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.messagebox import showwarning, showinfo
import PyPDF2
import os

class PdfHandler():
    def __init__(self):
        self.filepaths = []

    def merge_files(self):
        if len(self.filepaths) < 2:
            return "Não há arquivos suficientes"

        merger = PyPDF2.PdfMerger(strict=False)

        for filepath in self.filepaths:
            filename = os.path.basename(filepath)
            try:
                if filename.lower().endswith(".pdf"):
                    merger.append(filepath, outline_item=filename)
            except AttributeError:
                pass
        
        return merger
    
    def cut_file(self, index_str):
        if len(self.filepaths) != 1:
            return "Só é possível cortar apenas um arquivo"

        indexes = []
        try:
            for part in index_str.split(";"):
                if "-" in part:
                    start, end = map(int, part.split("-"))
                    indexes.extend(range(start, end + 1))
                else:
                    indexes.append(int(part))
        
        except:
            return "Preencha as páginas corretamente, como '3-5,10'"
        
        # abrir o arquivo
        filepath = self.filepaths[0]
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            writer = PyPDF2.PdfWriter()

            for i in indexes:
                try:
                    writer.add_page(reader.pages[i-1])
                except IndexError:
                    pass
            f.close()
        return writer

        

class App(tk.Tk):
    def __init__(self, handler:PdfHandler):
        super().__init__()
        
        # app
        self.minsize(450, 400)
        self.maxsize(450, 400)
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
        self.styler.configure("style2.TFrame", background="#141414")
        self.styler.configure("style2.TLabel", background="#141414", foreground="#5eeb00", font=self.font)

    def TButton2(self, *args, **kwargs):
        return tk.Button(*args, **kwargs, font=self.font, background="#141414", foreground="#5eeb00", width=12)
    
    def TEntry2(self, *args, **kwargs):
        return tk.Entry(*args, **kwargs, font=self.font, background="#141414", foreground="#5eeb00", width=15)

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
        line2 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line2.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line2, text="Nome do Arquivo criado:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.output_name_strgvar = tk.StringVar(value="output.pdf")
        self.TEntry2(line2, textvariable=self.output_name_strgvar).pack(side="right",padx=5, anchor="e")

        # ============ Linha 2 ============
        line1 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line1.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line1, text="Arquivos PDF Selecionados:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.TButton2(line1, text="Procurar", command=self.get_files).pack(side="right", padx=5, anchor="e")

        self.num_files_label = ttk.Label(line1, text="0", style="style2.TLabel")
        self.num_files_label.pack(side="right", padx=(0,5), anchor="e")

        # ============ Linha 3 ============
        line3 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line3.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line3, text="Limpar arquivos Selecionados:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.TButton2(line3, text="Limpar", command=self.clear_files).pack(side="right", padx=5, anchor="e")

        # ============ Linha 4 ============
        line4 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line4.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line4, text="Unir arquivos selecionados:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.TButton2(line4, text="Unir", command=self.merge_files).pack(side="right", padx=5, anchor="e")

        # ============ Linha 5 ============
        line5 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line5.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line5, text="Definir páginas para cortar:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.index_page_var = tk.StringVar(value="")
        self.TEntry2(line5, textvariable=self.index_page_var).pack(side="right",padx=5, anchor="e")

        # ============ Linha 6 ============
        line6 = ttk.Frame(self.inputframe, style="style2.TFrame")
        line6.pack(padx=5, pady=5, anchor="w", fill="x")

        ttk.Label(line6, text="Cortar arquivo selecionado:", style="style2.TLabel").pack(side="left", padx=(0,5), anchor="w")

        self.TButton2(line6, text="Cortar", command=self.cut_file).pack(side="right", padx=5, anchor="e")

    def get_files(self):
        filetypes = (
            ("Pdf files", ".pdf"),
            ("All files", "*.*")
        )

        files = filedialog.askopenfilenames(filetypes=filetypes)

        self.handler.filepaths.extend(files)

        self.num_files_label.config(text=str(len(self.handler.filepaths)))

    def clear_files(self):
        self.handler.filepaths = []
        self.num_files_label.config(text=str(len(self.handler.filepaths)))

    def merge_files(self):
        merger = self.handler.merge_files()

        if not isinstance(merger, str):
            # save_path = filedialog.askdirectory()
            # filename = self.output_name_strgvar.get()

            # if not filename.lower().endswith(".pdf"):
            #     filename += ".pdf"

            # save_path = os.path.join(save_path, filename)

            # with open(save_path, "wb") as f:
            #     merger.write(f)
            #     merger.close()

            # showinfo("Mensagem", f"Arquivo {filename} salvo!")
            self._save_pdf(merger)
        else:
            showwarning("Aviso", merger)
    
    def cut_file(self):
        writer = self.handler.cut_file(self.index_page_var.get())

        if not isinstance(writer, str):
            self._save_pdf(writer)
        else:
            showwarning("Aviso", writer)

    def _save_pdf(self, pdf):
        save_path = filedialog.askdirectory()
        filename = self.output_name_strgvar.get()

        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"

        save_path = os.path.join(save_path, filename)

        with open(save_path, "wb") as f:
            pdf.write(f)
            pdf.close()

        showinfo("Mensagem", f"Arquivo {filename} salvo!")

        




root = App(PdfHandler)
root.mainloop()