import tkinter as tk
from tkinter import ttk
from calculations import Calculations

class Model():
    def __init__(self, controller):
        self.controller = controller
        self.polygon = []

    def calculate_area(self):
        calc = Calculations(self.polygon)
        return calc.Area_of_Polygon()


class View(tk.Tk):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "title"
        self.controller = controller
        self.width, self.height = 1000, 800

        self.geometry(f"{self.width}x{self.height}")
        self.pack_propagate = False

        self.setup_gui()
        self.canvas_gui()
        self.input_gui()

        self.setup_styler()

    
    # ==== DEFINIR STILO DE ELEMENTOS TTK ====
    def setup_styler(self):
        self.styler = ttk.Style(self)
        self.styler.configure("TFrame", background="#f0f0f0")
        self.styler.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
        self.styler.configure("TButton", background="#f0f0f0", font=("Helvetica", 12))

    # ==== MÉTODOS QUE DEFINEM A PARTE VISUAL ====
    def setup_gui(self):
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(fill="both", expand=True)

        self.leftframe = ttk.Frame(self.mainframe)
        self.leftframe.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.rightframe = ttk.Frame(self.mainframe, width=300)
        self.rightframe.pack(side="left", fill="both", padx=5, pady=5)

        

    def canvas_gui(self):
        self.maincanvas = tk.Canvas(self.leftframe, bg="#dddddd", cursor="X_cursor")
        self.maincanvas.pack(fill="both", expand=True, padx=5, pady=5)
        self.maincanvas.config(takefocus=1)

        self.scale = 1
        self.rounder = 1

        self.last_point = None
        self.polygon = []
        self.ortho_mode = False

        self._bind_canvas_events()

    def input_gui(self):
        # titulo
        ttk.Label(
            self.rightframe, text="Titulo", font=("Helvetica", 20)
        ).pack(pady=10)

        # coordenadas
        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x", pady=5)

        coord_frame = ttk.Frame(self.rightframe)
        coord_frame.pack(fill="x", pady=5, padx=5)

        # Entrada para X
        ttk.Label(coord_frame, text="X:").pack(side="left")
        self.x_stringvar = tk.StringVar(value="0")
        ttk.Entry(coord_frame, textvariable=self.x_stringvar, width=8).pack(side="left", padx=(0, 10))

        # Entrada para Y
        ttk.Label(coord_frame, text="Y:").pack(side="left")
        self.y_stringvar = tk.StringVar(value="0")
        ttk.Entry(coord_frame, textvariable=self.y_stringvar, width=8).pack(side="left", padx=(0, 10))

        ttk.Button(self.rightframe, text="+Coordenada",command=self.controller.add_point_button).pack(pady=5, fill="x")

        # Escala
        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x", pady=5)

        self.scale_var = tk.IntVar(value=50)
        ttk.Label(self.rightframe, text="Definir Escala").pack(pady=5)
        ttk.Scale(self.rightframe, from_=0, to=100, variable=self.scale_var, command=self.update_scale).pack()

        # calcular
        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x", pady=5)

        ttk.Button(self.rightframe, text="Calcular!",command=self.controller.calculate_area).pack(pady=5, fill="x")

        self.area_label = ttk.Label(self.rightframe)
        self.area_label.pack(pady=5)
        

    # === COMANDOS DOS BOTÕES ===
    def update_scale(self, event):
        min_scale, max_scale = 0.001, 1000

        def map_value(x):
            normalized = x / 100
            return min_scale * ((max_scale / min_scale) ** normalized)

        scale_value = self.scale_var.get()

        self.scale = map_value(scale_value)

        self.update_screen()


    # ==== MÉTODOS DE EVENTOS DO CANVAS ==== 
    def _bind_canvas_events(self):
        self.maincanvas.bind("<Button-1>", self._Button1_clicked)
        self.maincanvas.bind("<Motion>", self._mouse_motion)
        for i in ("<Escape>", "<Button-3>", "<space>"):
            self.maincanvas.bind(i, self._polygon_done)

        self.maincanvas.bind("<F8>", self._f8_pressed)
    
    def add_new_point(self, point, is_canvas = True):
        if not is_canvas:
            point = self._convert_to_canvas_coords(point)

        # checar se é o início de um polígono
        if self.last_point is None:
            
            self.last_point = self._convert_from_canvas_coords(point)
            self.polygon = [self.last_point]
        else:
            self.last_point = self._handle_ortho_mode(point, convert_from_canvas=True)
            if self.last_point == self.polygon[0]:
                self._polygon_done(None)
                
                return

            self.polygon.append(self.last_point)
        
        
        self.update_screen()
        self.maincanvas.focus_set()

    def _Button1_clicked(self, event):
        self.maincanvas.focus_set()
        point = (event.x, event.y)

        self.add_new_point(point)
         

    def _mouse_motion(self, event):
        temp_canvas_point = self._handle_ortho_mode((event.x, event.y), convert_from_canvas=False)
        
        
        self._draw_coord_at_point(temp_canvas_point)

        
        # só queremos que seja desenhado se o polígono
        # foi iniciado
        if self.last_point is None:
            return

        last_canvas_point = self._convert_to_canvas_coords(self.last_point)
        
        self.maincanvas.create_line(last_canvas_point, temp_canvas_point, fill="black", width=5)

    def _polygon_done(self, event):
        
        # close polygon
        self.polygon.append(self.polygon[0])

        # reset lines
        self.last_point = None

        # update canvas
        self.draw_canvas()
        
        self.controller.set_polygon(self.polygon)
    
    def _f8_pressed(self, event):
        self.ortho_mode = not self.ortho_mode

    # ==== HELPER METHODS ====
    def _handle_ortho_mode(self, canvas_point, convert_from_canvas:bool=True):
        if self.last_point is None:
            pass
        elif self.ortho_mode:
            x, y = canvas_point
            x0, y0 = self._convert_to_canvas_coords(self.last_point)

            if abs(x - x0) > abs(y - y0):
                canvas_point = (x, y0)
            else:
                canvas_point = (x0, y)

        if convert_from_canvas:
            return self._convert_from_canvas_coords(canvas_point)
        else:
            return canvas_point
        
    def _draw_coord_at_point(self, canvas_point, canvas=None):
        if canvas is None:
            canvas = self.maincanvas

        x, y = self._convert_from_canvas_coords(canvas_point)
        self.draw_canvas()
        canvas.create_text(canvas_point, text=f"({x}, {y})", anchor="sw", fill="blue")

    def _convert_to_canvas_coords(self, point, canvas = None, scale = None):
        if canvas is None:
            canvas = self.maincanvas
        if scale is None:
            scale = self.scale
        
        w, h = canvas.winfo_width(), canvas.winfo_height()

        x, y = point

        x_canvas = x * scale + (w / 2)
        y_canvas = -1 * y * scale + h/2 

        return x_canvas, y_canvas

    def _convert_from_canvas_coords(self, canvas_point, canvas = None, scale = None, rounder = None):
        if rounder is None:
            rounder = self.rounder
        if canvas is None:
            canvas = self.maincanvas
        if scale is None:
            scale = self.scale
        
        w, h = canvas.winfo_width(), canvas.winfo_height()

        x_canvas, y_canvas = canvas_point # em canvas

        x = round((x_canvas - (w / 2)) / scale, rounder)
        y = round((h / 2 - y_canvas) / scale, rounder)

        return x, y


    # ==== MÉTODOS DE DESENHO E ATUALIZAÇÃO ====

    def draw_canvas(self):
        # deletar desenhos anteriores
        self.maincanvas.delete("all")
        
        # obter tamanho do canvas
        canvas_w, canvas_h = self.maincanvas.winfo_width(), self.maincanvas.winfo_height()
                
        top_left = self._convert_from_canvas_coords((0, 0))
        bottom_right = self._convert_from_canvas_coords((canvas_w, canvas_h))

        largura = bottom_right[0] - top_left[0]
        altura = top_left[1] - bottom_right[1] 


        if len(self.polygon) > 1:
            canvas_polygon = [self._convert_to_canvas_coords(i) for i in self.polygon]
            self.maincanvas.create_line(*canvas_polygon, width=3, fill="black")

            if self.last_point is None: # o polígono está fechado 
                self.maincanvas.create_polygon(*canvas_polygon, width=3, fill="red")
        
        # desenhar eixos
        self.maincanvas.create_line((0, canvas_h/2), (canvas_w, canvas_h/2), width=1, fill="black")
        self.maincanvas.create_line((canvas_w/2, 0), (canvas_w/2, canvas_h), width=1, fill="black")

        self.maincanvas.create_text((0 + canvas_w *.01,0 + canvas_h *.01), text=f"{largura}x{altura}", anchor="nw")

    def update_screen(self):
        self.draw_canvas()
    
    

class Controller(object):
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)

        self.view.maincanvas.bind("<Configure>", self.update_screen)
        
    def update_screen(self, event):
        self.view.update_screen()

    def set_polygon(self, new_polygon):
        self.model.polygon = new_polygon

    def add_point_button(self):
        x = self.view.x_stringvar.get()
        y = self.view.y_stringvar.get()
        try:
            x = float(x)
            y = float(y)
        except:
            return

        self.view.add_new_point((x, y), is_canvas=False)

    def calculate_area(self):
        if len(self.view.polygon) > 2:
            area = self.model.calculate_area()

            self.view.area_label.config(text=f"Área: {area}")
    
    def run(self):
        self.view.mainloop()


App = Controller()
App.run()