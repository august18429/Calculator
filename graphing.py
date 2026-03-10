import matplotlib.pyplot as plt
import numpy as np

equation = input("Enter equation in the form y = mx + b")

equation = equation.replace(" ", "")

equation = equation.replace("y=", "")
parts = equation.split("x")

m = float(parts[0])
b = float(parts[1]) if parts[1] else 0

x = np.linspace(-5,5,100)

y = m * x + b

plt.plot(x, y, label=f'y = {m}x + {b}')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")
plt.grid(True)
plt.legend()
plt.show()