import numpy as np

N = int(input('Сколько строк? '))
M = int(input('Сколько столбцов? '))

a = np.zeros( (N, M) )

for i in range(N):
  for j in range(M):
    a[i][j] = int(input(f"Введите a[{i}][{j}] элемент"))

# Решение есть, но плохое. Писать не хочу, пока не придумаю новое