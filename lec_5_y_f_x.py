import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0, title="plotter"):
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label="my parabola")
    plt.legend()
    plt.title(title)
    plt.show()

parabola_plotter()