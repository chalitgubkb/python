data = [10,20,30,40,50]
print('data = ',data)

data2 = [60,70,80,90,100]
print('data2 = ',data2)

print('data + data2 = ',data+data2)

data.extend(data2)
print('data = ',data)