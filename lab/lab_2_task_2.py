first = int(input())
znam = int(input())
count = int(input())

string = f'{first} '
last = first

for i in range(count - 1):
  last *= znam
  string += str(last) + ' '

print(string)