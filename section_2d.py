import numpy as np
import matplotlib.pyplot as plt

epsilon = 0.1
u = np.linspace(epsilon, np.pi / 2 - epsilon, 100)

x_circle = np.cos(u)
y_circle = np.sin(u)
plt.plot(x_circle, y_circle)

rho = np.sin(epsilon) / np.minimum(np.sin(u), np.cos(u))

x_line = rho * np.cos(u)
y_line = rho * np.sin(u)

plt.plot(x_line, y_line)

plt.axes().set_aspect('equal')
plt.show()
