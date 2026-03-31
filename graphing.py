import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import re
import warnings
import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)



warnings.filterwarnings("ignore")

class GraphWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title('Graph')

        self.fig = Figure(figsize=(6,5))
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        
        self.canvas.get_tk_widget().pack(fill='both',expand=True)

        self.toolbar=NavigationToolbar2Tk(self.canvas, self.window)
        self.toolbar.update()

        self.controls = tk.Frame(self.window)
        self.controls.pack()

        tk.Button(self.controls, text='Find Intersections',
                  command=self.find_intersections).pack(side='left')
        self.derivative_button = tk.Button(
            self.controls, text='Show Derivative',
            command=self.plot_derivative, state='disabled'
        )
        self.derivative_button.pack(side='left')
        tk.Button(self.controls, text='Shade Integral',
                  command=lambda: self.shade_integral(-2,2)).pack(side='left')
        tk.Button(self.controls, text='Reset Graph',
                  command=lambda: self.update_graph(self.equations)).pack(side='left')

        tk.Label(self.controls,text='Integral from').pack(side='left')

        self.int_a = tk.Entry(self.controls,width=5)
        self.int_a.insert(0,'-2')
        self.int_a.pack(side='left')
        tk.Label(self.controls,text='to').pack(side='left')

        self.int_b = tk.Entry(self.controls, width=5)
        self.int_b.insert(0,'2')
        self.int_b.pack(side='left')

        tk.Button(self.controls,text='Shade',
                  command=self.integral_button).pack(side='left')

        self.trace_label = tk.Label(self.window,
                                    text='Trace: Use arrow keys')
        self.trace_label.pack()


        self.slider_frame = tk.Frame(self.window)
        self.slider_frame.pack()

        tk.Label(self.slider_frame, text='a')

        self.a_slider = tk.Scale(
            self.slider_frame,
            from_=-10,
            to=10,
            orient='horizontal',
            command=self.slider_update
        )

        self.a_slider.set(1)
        self.a_slider.pack(side='left')

        self.trace_index = 0
        self.trace_line = None
        self.trace_point = None

        self.equations = []

        self.x_vals = None
        self.y_values = []

        self.window.bind('<Left>', self.trace_left)
        self.window.bind('<Right>',self.trace_right)

    def integral_button(self):
        try:
            a = float(self.int_a.get())
            b = float(self.int_b.get())
            self.shade_integral(a,b)
        except:
            pass
    def slider_update(self,val):
        if self.equations:
            self.update_graph(self.equations)

    def update_graph(self, equations):
        self.equations = equations
        self.ax.clear()

        x = np.linspace(-10,10,400)

        self.x_vals = x
        
        a = self.a_slider

        colors = ['red','blue','green','purple','black']

        self.y_values = []

        for eq,color in zip(equations,colors):

            if eq.strip() == "":
                continue
            display_eq = eq

            eq = eq.replace('^','**')

            eq = re.sub(r'(\d)x', r'\1*x', eq)

            try:
                sym_x = sp.symbols('x')
                transformations = standard_transformations + (implicit_multiplication_application,)
                expr = parse_expr(eq, transformations=transformations)
                func = sp.lambdify(sym_x, expr, 'numpy')
                y = func(x)
                self.ax.plot(x,y, label=display_eq, color=color)
                self.y_values.append(y)
            except Exception as e:
                pass
        self.ax.axhline(0,color='black')
        self.ax.axvline(0,color='black')

        self.ax.grid(True)
        self.ax.legend()

        self.ax.set_xlim(-10,10)
        self.ax.set_ylim(-10,10)
        if hasattr(self, 'show_intersections') and self.show_intersections:
            self.find_intersections()
        
        self.canvas.draw()
    def draw_trace(self):
        if not self.y_values:
            return
        y = self.y_values[0]

        x = self.x_vals[self.trace_index]
        y_val = y[self.trace_index]

        if self.trace_point:
            self.trace_point.remove()

        self.trace_point = self.ax.plot(x,y_val, 'ko')[0]

        self.ax.set_title(f"x={x:.2f} y={y_val:.2f}")
    def trace_left(self,event):
        if self.trace_index > 0:
            self.trace_index -= 1
            self.draw_trace()
            self.canvas.draw()
    def trace_right(self,event):
        if self.trace_index < len(self.x_vals)-1:
            self.trace_index += 1
            self.draw_trace()
            self.canvas.draw()
    def find_intersections(self):
        self.show_intersections = True
    def draw_intersections(self):
        if len(self.y_values) < 2:
            return
        y1 = self.y_values[0]
        y2 = self.y_values[1]

        diff = y1 - y2

        roots = np.where(np.diff(np.sign(diff)))[0]

        for r in roots:

            x = self.x_vals[r]
            y = y1[r]

            self.ax.plot(x,y,'ro')

    def plot_derivative(self):
        if self.x_vals is None or not self.y_values:
            print('Graph a function first')
            return
        y = self.y_values[0]

        dy = np.gradient(y, self.x_vals)

        self.ax.plot(self.x_vals, dy, color='orange', label='Derivative')

        self.ax.legend()

        self.canvas.draw()
    def shade_integral(self,a,b):
        if self.x_vals is None or not self.y_values:
            print('Graph a function first.')
            return
        y = self.y_values[0]

        mask = (self.x_vals >= a) & (self.x_vals <= b)

        self.ax.fill_between(self.x_vals[mask], y[mask], alpha=0.3)

        self.canvas.draw()
