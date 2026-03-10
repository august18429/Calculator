import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

PYGAME_DETECT_AVX2=1

table = pd.DataFrame(
    {
        "f(x)": [" "],
        "g(x)": [" "],
        "h(x)": [" "],
        "b(x)": [" "],
        "r(x)": [" "]
    }
)

def open_graph():
    print('Running code via exec():')
    with open("graphing.py", "r") as f:
        code = f.read()
        exec(code)
def close_window():
    sys.exit(0)
extras = ["Okay", "Cancel"]
from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root)
#frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Equations:")
flbl = ttk.Label(content, text="f(x) =")
glbl = ttk.Label(content, text="g(x) =")
hlbl = ttk.Label(content, text="h(x) =")
blbl = ttk.Label(content, text="b(x) =")
rlbl = ttk.Label(content, text="r(x) =")
f = ttk.Entry(content)
g = ttk.Entry(content)
h = ttk.Entry(content)
b = ttk.Entry(content)
r = ttk.Entry(content)


onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay", command=open_graph)
cancel = ttk.Button(content, text="Cancel", command=close_window)

content.grid(column=0, row=0)
#frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
f.grid(column=3,row=0, columnspan=2)
g.grid(column=3, row=1, columnspan=2)
h.grid(column=3, row=2, columnspan=2)
b.grid(column=3, row=3, columnspan=2)
r.grid(column=3, row=4, columnspan=2)
flbl.grid(column=1,row = 0, columnspan=2)
glbl.grid(column=1,row = 1, columnspan=2)
hlbl.grid(column=1,row = 2, columnspan=2)
blbl.grid(column=1,row = 3, columnspan=2)
rlbl.grid(column=1,row = 4, columnspan=2)
ok.grid(column=1, row=5, columnspan=2)
cancel.grid(column=4, row=5, columnspan=2)

content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()

