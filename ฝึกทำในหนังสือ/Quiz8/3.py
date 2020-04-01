import os
os.system('color 9')
os.system('cls')

data = {32,8,9,12,14,-4,54,26,19}
print('data = ',data)

data2 = {14,32,80,-2}

print('data = ',data2)
print('len = ',len(data))
print('max = ',max(data))
print('min = ',min(data))
print('sum = ',sum(data))
print('union = ',data.union(data2))
print('intersection = ',data.intersection(data2))
print('difference = ',data.difference(data2))

#ผลลัพธ์จะได้
# data =  {32, 8, 9, 12, 14, 19, 54, 26, -4}
# data =  {32, 80, 14, -2}
# len =  9
# max =  54
# min =  -4
# sum =  170
# union =  {32, 8, 9, 12, 14, 80, 19, 54, 26, -4, -2}
# intersection =  {32, 14}
# difference =  {8, 9, 12, 19, 54, 26, -4}