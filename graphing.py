import matplotlib.pyplot as plt
import numpy as np
import table
import Calculator


#Importing each equation from the table.py file
f_line = table.f
g_line = table.g
h_line = table.h
b_line = table.b
r_line = table.r

#Getting rid of spaces in the equations
f_equation = f_line.replace(" ", "")
g_equation = g_line.replace(" ", "")
h_equation = h_line.replace(" ", "")
b_equation = b_line.replace(" ", "")
r_equation = r_line.replace(" ", "")

#Getting rid of "y=" if the user included it
f_equation = f_equation.replace("y=", "")
g_equation = g_equation.replace("y=", "")
h_equation = h_equation.replace("y=", "")
b_equation = b_equation.replace("y=", "")
r_equation = r_equation.replace("y=", "")

#Splits each equation
f_parts = f_equation.split("x")
g_parts = g_equation.split("x")
h_parts = h_equation.split("x")
b_parts = b_equation.split("x")
r_parts = r_equation.split("x")

f_m = float(f_parts[0])
f_b = float(f_parts[1]) if f_parts[1] else 0

g_m = float(g_parts[0])
g_b = float(g_parts[1]) if g_parts[1] else 0

h_m = float(h_parts[0])
h_b = float(h_parts[1]) if h_parts[1] else 0

b_m = float(b_parts[0])
b_b = float(b_parts[1]) if b_parts[1] else 0

r_m = float(r_parts[0])
r_b = float(r_parts[1]) if r_parts[1] else 0

x = np.linspace(-5,5,100)

f_y = f_m * x + f_b
g_y = g_m * x + g_b
h_y = h_m * x + h_b
b_y = b_m * x + b_b
r_y = r_m * x + r_b

plt.plot(x, f_y, label=f'y = {f_m}x + {f_b}', color=Calculator.color_red)
plt.plot(x, g_y, label=f'y = {g_m}x + {g_b}', color=Calculator.color_blue)
plt.plot(x, h_y, label=f'y = {h_m}x + {h_b}', color=Calculator.color_green)
plt.plot(x, b_y, label=f'y = {b_m}x + {b_b}', color=Calculator.color_purple)
plt.plot(x, r_y, label=f'y = {r_m}x + {r_b}', color=Calculator.color_black)



plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")
plt.grid(True)
plt.legend()
plt.show()