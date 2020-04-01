import os
os.system('cls')
os.system('color 9')
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