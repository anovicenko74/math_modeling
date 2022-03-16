import numpy as np
G = 9.8

t = np.arange(0, 5, 0.1)

x0 = float(input())
u0x = float(input())

x = x0 + u0x * t
print(x, ' - x')

y0 = float(input())
u0y = float(input())

y = y0 + u0y * t - (G*t**2) / 2

print(y, ' - y')

coords = np.zeros((len(t), 3))

for i in range(len(t)):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]
