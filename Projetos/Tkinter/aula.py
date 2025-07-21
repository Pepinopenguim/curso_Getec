import tkinter as tk
from tkinter import ttk
from calculations import Calculations

class Model():
    def __init__(self, controller):
        self.controller = controller
        self.polygon = []
    
    def calc_area(self):
        c = Calculations(self.polygon)
        return c.Area_of_Polygon()
    
    def calc_report(self):
        c = Calculations(self.polygon, round_value=2)
        return c.Report()

    

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.width, self.height = 1000, 800

        self.geometry(f"{self.width}x{self.height}")
        
        self.polygon = None
        self.last_point = None

        self.setup_gui()
        self.canvas_gui()
        self.input_gui()

        self.setup_styler()

    def setup_styler(self):
        self.styler = ttk.Style(self)
        self.styler.configure("TFrame", background="#c2feff")
        self.styler.configure("TLabel", background="#c2feff", font=("Consolas", 12))
        self.styler.configure("TButton", background="#c2feff", foreground="#192424", relief="flat", font=("Consolas", 12))
        self.styler.configure("TScale", background="#c2feff")

    def setup_gui(self):
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(fill="both", expand=True)

        self.leftframe = ttk.Frame(self.mainframe)
        self.leftframe.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.rightframe = ttk.Frame(self.mainframe, width=300)
        self.rightframe.pack(side="left", fill="both", padx=5, pady=5)

    def canvas_gui(self):
        self.maincanvas = tk.Canvas(self.leftframe, bg="#99e4e5")
        self.maincanvas.pack(fill="both", expand=True, padx=5, pady=5)
        self.maincanvas.config(takefocus=1)
        self._bind_canvas_events()

        self.scale = .5

    def input_gui(self):
        # titulo
        ttk.Label(
            self.rightframe,
            text="CALCULADORA DE\nPOLÍGONOS",
            font=("Consolas", 20, "bold")
        ).pack(pady=10)

        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x", pady=5)

        coord_frame = ttk.Frame(self.rightframe)
        coord_frame.pack(fill="x", pady=5, padx=5)

        # entrada pra x
        ttk.Label(coord_frame, text="X:").pack(side="left")
        self.x_strgvar = tk.StringVar(value="0")
        ttk.Entry(
            coord_frame,
            width=6,
            font=("consolas", 16), 
            textvariable=self.x_strgvar
        ).pack(side="left", padx=(0,10))

        # entrada pra y
        ttk.Label(coord_frame, text="Y:").pack(side="left")
        self.y_strgvar = tk.StringVar(value="0")
        ttk.Entry(
            coord_frame,
            width=6,
            font=("consolas", 16),
            textvariable=self.y_strgvar
        ).pack(side="left", padx=(0,10))

        # botão de adicionar
        ttk.Button(self.rightframe, text="+Coordenada", command=self.controller.add_coord).pack(padx=5, pady=5, fill="x")

        # escala
        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x", pady=5)
        ttk.Label(
            self.rightframe,
            text="Definir Escala"
        ).pack(fill="x", pady=5, anchor="center")

        self.scale_var = tk.IntVar(value=50)
        ttk.Scale(self.rightframe, from_=0, to=100, variable=self.scale_var, command=self.update_scale).pack(pady=5, fill="x")

        # calcular
        ttk.Separator(self.rightframe, orient=tk.HORIZONTAL).pack(fill="x", pady=5)

        ttk.Button(self.rightframe, text="Calcular!", command=self.controller.calculate).pack(pady=5, fill="x")

        self.area_label = ttk.Label(self.rightframe, text="", font=("consolas", 15, "bold"))
        self.area_label.pack(pady=5)

    def _bind_canvas_events(self):
        self.maincanvas.bind("<Button-1>", self._mouse_click)
        self.maincanvas.bind("<Motion>", self._mouse_motion)
        self.maincanvas.bind("<space>", self._polygon_done)

    def update_scale(self, event):
        self.controller.change_scale()

    def _mouse_click(self, event):
        self.maincanvas.focus_set()

        canvas_point = (event.x, event.y)
        point = self._convert_from_canvas_coords(canvas_point)

        self._add_point(point)
    
    def _add_point(self, point):
        # checa se é o primeiro ponto
        if self.last_point is None:
            self.area_label.configure(text=f"")
            self.last_point = point
            self.polygon = [self.last_point]
        else:
            self.last_point = point
            self.polygon.append(self.last_point)

        self.update_screen()
        self.maincanvas.focus_set()

    def _mouse_motion(self, event):
        canvas_point = (event.x, event.y)
        self._draw_coord_at_point(canvas_point)

        if self.last_point is None:
            return
        
        last_canvas_point = self._convert_to_canvas_coords(self.last_point)

        
        self.maincanvas.create_line(last_canvas_point, canvas_point, fill="blue", width=5)
    
    def _draw_coord_at_point(self, canvas_point):
        x, y = self._convert_from_canvas_coords(canvas_point)

        canvas_w = self.maincanvas.winfo_width()

        anchor = "sw" if canvas_point[0] < .9*canvas_w else "se"

        self.draw_canvas()
        self.maincanvas.create_text(canvas_point, text=f"({x:.2f}x{y:.2f})", anchor=anchor, fill="#1f3838")

    def _polygon_done(self, event):
        if len(self.polygon) < 3:
            return
            
        self.polygon.append(self.polygon[0])
        self.last_point = None

        self.draw_canvas()

        self.controller.save_polygon()
    
    def _convert_from_canvas_coords(self, canvas_point):
        canvas_w = self.maincanvas.winfo_width()
        canvas_h = self.maincanvas.winfo_height()

        x_canvas, y_canvas = canvas_point
        
        x = (x_canvas - canvas_w / 2) / self.scale
        y = (canvas_h / 2 - y_canvas) / self.scale

        return (x, y)
        

    def _convert_to_canvas_coords(self, point):
        canvas_w = self.maincanvas.winfo_width()
        canvas_h = self.maincanvas.winfo_height()

        x, y = point

        x_canvas = x * self.scale + canvas_w / 2
        y_canvas = -1 * y * self.scale + canvas_h/2

        return (x_canvas, y_canvas)

    def draw_canvas(self):
        self.maincanvas.delete("all")


        canvas_w = self.maincanvas.winfo_width()
        canvas_h = self.maincanvas.winfo_height()

        if self.polygon is not None:
            if len(self.polygon) > 1:
                polygon_canvas = []
                for p in self.polygon:
                    canvas_p = self._convert_to_canvas_coords(p)
                    polygon_canvas.append(canvas_p)

                # checar se o polygono esta fechado
                if self.last_point is None:
                    self.maincanvas.create_polygon(*polygon_canvas, fill="#1d9c9c")

                self.maincanvas.create_line(*polygon_canvas, width=3, fill="#152424")


        # desenhar os eixos das coordenadas
        self.maincanvas.create_line((0,canvas_h/2), (canvas_w, canvas_h/2), width=1, fill="black")
        self.maincanvas.create_line((canvas_w / 2,0), (canvas_w/2, canvas_h), width=1, fill="black")

        self.maincanvas.create_text((canvas_w*.98, canvas_h/2), text="x", anchor="s", font=("consolas", 15))
        self.maincanvas.create_text((canvas_w/2 * 1.02, canvas_h * .02), text="y", anchor="w", font=("consolas", 15))

    def update_screen(self):
        self.draw_canvas()



class Controller():
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)

        self.view.maincanvas.bind("<Configure>", self.update_screen)

    def save_polygon(self):
        if len(self.view.polygon) > 2:
            self.model.polygon = self.view.polygon

    def change_scale(self):
        min_scale, max_scale = .001, 100000
        # x varia de 0 a 100
        def map_value(x):
            normalized = x / 100
            return min_scale * ((max_scale / min_scale) ** normalized)
        
        new_scale = map_value(self.view.scale_var.get())

        self.view.scale = new_scale
        self.view.draw_canvas()

    def add_coord(self):
        # pegar os valores de x e y da entry
        x = self.view.x_strgvar.get()
        y = self.view.y_strgvar.get()

        try:
            x = float(x)
            y = float(y)
        except:
            return
        
        # adicionar o ponto
        self.view._add_point((x, y))

    def calculate(self):
        # checar se o poligono está salvo
        if not self.model.polygon:
            return
        report = self.model.calc_report()
        report = report.replace("-", "")
        self.view.area_label.configure(text=report)

    def update_screen(self, event):
        self.view.update_screen()

    def run(self):
        self.view.mainloop()


App = Controller()
App.run()