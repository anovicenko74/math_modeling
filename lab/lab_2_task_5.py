num1 = int(input('Число '))
num2 = int(input('Его делитель '))

if num2:
  if (num1 % num2 == 0):
    print(f'Все делится без остатка - {num1 // num2}')
  else:
    print(f'Целая часть - {num1 // num2}, Остаток - {num1 % num2}')

