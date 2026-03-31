import tkinter as tk
import graphing
import sympy as sp

def open_table(parent):
    table_window = tk.Toplevel(parent)
    table_window.title('Equations')

    labels = ['f(x) =', 'g(x) =', 'h(x) =', 'b(x) =', 'r(x) =']

    entries = []

    graph = graphing.GraphWindow(parent)

    for i,label in enumerate(labels):
        tk.Label(table_window,text=label).grid(row=i,column=0)

        entry = tk.Entry(table_window,width=20)
        entry.grid(row=i,column=1)

        entries.append(entry)
    def update_graph(event=None):
        equations = [e.get() for e in entries]

        graph.update_graph(equations)
    for entry in entries:
        entry.bind('<KeyRelease>', update_graph)
    tk.Button(table_window,text='Close',command=table_window.destroy).grid(row=6,column=0)

