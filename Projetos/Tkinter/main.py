import tkinter as tk
from tkinter import ttk

class Model():
    def __init__(self, controller):
        self.controller = controller
        self.polygon = []


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
        self.styler.configure("TLabel", background="#f0f0f0", font=("Helvetica", 16))
        self.styler.configure("TEntry", background="#f0f0f0")
        self.styler.configure("TButton", background="#f0f0f0")

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

        self.scale = 10
        self.rounder = 1

        self.last_point = None
        self.polygon = []
        self.ortho_mode = False

        self._bind_canvas_events()

        
    def _bind_canvas_events(self):
        self.maincanvas.bind("<Button-1>", self._Button1_clicked)
        self.maincanvas.bind("<Motion>", self._mouse_motion)
        for i in ("<Escape>", "<Button-3>", "<space>"):
            self.maincanvas.bind(i, self._esc_pressed)

        self.maincanvas.bind("<F8>", self._f8_pressed)

    def input_gui(self):
        # title
        ttk.Label(
            self.rightframe, text="Titulo", font=("Helvetica", 20)
        ).pack(pady=10)

        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x")

        line1 = ttk.Frame(self.rightframe)
        line1.pack(side="top", padx=5, pady=5, fill="x")

        line2 = ttk.Frame(self.rightframe)
        line2.pack(side="top", padx=5, pady=5, fill="x")
        
        self.coord_strgvar = tk.StringVar(value="x;y")

        ttk.Label(line1, text="Nova Coordenada").pack(side="left")
        ttk.Entry(line2, textvariable=self.coord_strgvar, width=6, font=("Helvetica", 16)).pack(side="left", padx=5)

    
    # ==== MÉTODOS DE EVENTOS DO CANVAS ====
    def _Button1_clicked(self, event):
        self.maincanvas.focus_set()

        w, h = self.maincanvas.winfo_width(), self.maincanvas.winfo_height()
        
        # checar se é o início de um polígono
        if self.last_point is None:
            
            self.last_point = self._convert_from_canvas_coords((event.x, event.y))
            self.polygon = [self.last_point]
        else:
            self.last_point = self._handle_ortho_mode((event.x, event.y), convert_from_canvas=True)
            self.polygon.append(self.last_point)

    def _mouse_motion(self, event):
        temp_canvas_point = self._handle_ortho_mode((event.x, event.y), convert_from_canvas=False)
        
        
        self._draw_coord_at_point(temp_canvas_point)

        
        # só queremos que seja desenhado se o polígono
        # foi iniciado
        if self.last_point is None:
            return

        last_canvas_point = self._convert_to_canvas_coords(self.last_point)
        
        self.maincanvas.create_line(last_canvas_point, temp_canvas_point, fill="black", width=5)

    def _esc_pressed(self, event):
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
    def _draw_axis(self):
        canvas_w, canvas_h = self.maincanvas.winfo_width(), self.maincanvas.winfo_height()
        # desenhar eixos
        self.maincanvas.create_line((0, canvas_h/2), (canvas_w, canvas_h/2), width=1, fill="black")
        self.maincanvas.create_line((canvas_w/2, 0), (canvas_w/2, canvas_h), width=1, fill="black")

        # desenhar quebras de axis
        epsilon_x, epsilon_y = canvas_w/100, canvas_h/100

        min_x, max_y = self._convert_from_canvas_coords((0, 0))
        max_x, min_y = self._convert_from_canvas_coords((canvas_w, canvas_h))

    
        def norm_range(i0, i1, k)->int:
            i0 = int(i0 / k) * k
            i1 = int(i1 / k) * k

            return range(i0, i1, k)

        for xi in norm_range(min_x, max_x, 5):
            canvas_xi, y0 = self._convert_to_canvas_coords((xi, 0))
            self.maincanvas.create_line((canvas_xi, y0 - epsilon_y), (canvas_xi, y0 + epsilon_y))

        for yi in norm_range(min_y, max_y, 5):
            x0, canvas_yi = self._convert_to_canvas_coords((0, yi))
            self.maincanvas.create_line((x0 - epsilon_x, canvas_yi), (x0 + epsilon_x, canvas_yi))




        


    def draw_canvas(self):
        # deletar desenhos anteriores
        self.maincanvas.delete("all")
        
        # obter tamanho do canvas
        canvas_w, canvas_h = self.maincanvas.winfo_width(), self.maincanvas.winfo_height()


        if len(self.polygon) > 1:
            canvas_polygon = [self._convert_to_canvas_coords(i) for i in self.polygon]
            self.maincanvas.create_line(*canvas_polygon, width=3, fill="black")

            if self.last_point is None: # o polígono está fechado 
                self.maincanvas.create_polygon(*canvas_polygon, width=3, fill="red")
        
        self._draw_axis()

      

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
    
    def run(self):
        self.view.mainloop()


App = Controller()
App.run()