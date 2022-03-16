import numpy as np

n = int(input("Длина массива - "))

a = np.zeros(n)

for i in range(n):
  a[i] = int(input(f"Введите {i} элемент - "))

num = int(input("Новое число - "))
index = int(input("Индекс - "))

b = np.zeros(n + 1)

flag = False
for i in range(n + 1):
  if index != i and flag == False:
    b[i] = a[i]

  if flag:
    b[i] = a[i - 1]
    
  if index == i:
    b[i] = num
    flag = True

  

print(b)
  