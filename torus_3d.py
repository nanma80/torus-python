import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Generate torus mesh
angle = np.linspace(0, 2 * np.pi, 32)

epsilon = 0.1
limit = 2

u_range = np.linspace(epsilon, np.pi / 2 - epsilon, 16)
v_range = np.linspace(0, 2 * np.pi, 32)

u, v = np.meshgrid(u_range, angle)
r, R = 0.5, 1

x_circle = np.cos(u + v)
y_circle = np.sin(u + v)

X0 = (R + r * x_circle) * np.cos(v)
Y0 = (R + r * x_circle) * np.sin(v)
Z0 = r * y_circle

fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.set_xlim3d(-limit, limit)
ax.set_ylim3d(-limit, limit)
ax.set_zlim3d(-limit, limit)

rho = np.sin(epsilon) / np.minimum(np.sin(u), np.cos(u))
# rho = np.sin(epsilon) / np.sin(u)

x_line = rho * np.cos(u + v)
y_line = rho * np.sin(u + v)

X1 = (R + r * x_line) * np.cos(v)
Y1 = (R + r * x_line) * np.sin(v)
Z1 = r * y_line

X = np.concatenate((X0, X1))
Y = np.concatenate((Y0, Y1))
Z = np.concatenate((Z0, Z1))

ax.plot_surface(X, Y, Z, color = 'w', rstride = 1, cstride = 1)


# ax.set_aspect('equal')
plt.show()
