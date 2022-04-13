import matplotlib.pyplot as plt
import numpy as np

def parabola(a=1, b=1, c=0, title="plotter"):
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label="my parabola")
    plt.legend()
    plt.title(title)
    plt.show()

def giperbola(k=1):
  x = np.arange(-100, 100, 0.1)
  y = k / x
  print(y)
  plt.plot(x, y, label="my giper")
  plt.legend()
  plt.show()

giperbola() 
parabola()