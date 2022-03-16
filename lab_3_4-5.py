# A[i, j] = sin(N · (i+1) + M · (j + 1))

import math
import numpy as np

vector_1_len = int(input())
vector_2_len = int(input())

a = np.ones(( vector_1_len, vector_2_len ))

for i in range(vector_1_len):
  for j in range(vector_2_len):
    a[i][j] = math.sin(vector_1_len * (i+1) \
    + + vector_2_len * (j + 1));
    if a[i][j] < 0:
      a[i][j] = 0;

print('Начальный -', a, '\n')

t = np.zeros( (vector_1_len, vector_2_len) )
# меняем всего два столбца
t[0][::1] = a[1][::1]
t[1][::1] = a[0][::1]

print('Перевернутый -', t)