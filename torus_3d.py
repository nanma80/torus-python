import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# from stl import mesh

def get_torus_surface(is_circle, phase):
  epsilon = 0.1

  u_range = np.linspace(epsilon, np.pi / 2 - epsilon, 32)
  v_range = np.linspace(0, 2 * np.pi, 32)
  u, v = np.meshgrid(u_range, v_range)
  r, R = 0.5, 1

  if is_circle:
    rho = np.sin(epsilon) / np.minimum(np.sin(u), np.cos(u))
  else:
    rho = 1

  x = rho * np.cos(u + v + phase)
  y = rho * np.sin(u + v + phase)

  X = (R + r * x) * np.cos(v)
  Y = (R + r * x) * np.sin(v)
  Z = r * y
  return X, Y, Z


def get_branch(phase):
  X0, Y0, Z0 = get_torus_surface(True, phase)
  X1, Y1, Z1 = get_torus_surface(False, phase)
  X = np.concatenate((X0, X1))
  Y = np.concatenate((Y0, Y1))
  Z = np.concatenate((Z0, Z1))
  return X, Y, Z


def get_branches():
  X, Y, Z = None, None, None
  for i in xrange(4):
    X1, Y1, Z1 = get_branch(i * np.pi / 2)
    if X is None:
      X, Y, Z = X1, Y1, Z1
    else:
      X = np.concatenate((X, X1))
      Y = np.concatenate((Y, Y1))
      Z = np.concatenate((Z, Z1))
  return X, Y, Z


def plot():
  limit = 1.2
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.set_xlim3d(-limit, limit)
  ax.set_ylim3d(-limit, limit)
  ax.set_zlim3d(-limit, limit)

  X, Y, Z = get_branches()

  ax.plot_surface(X, Y, Z, color='w', rstride=1, cstride=1)
  ax.set_aspect('equal')
  plt.show()


plot()
