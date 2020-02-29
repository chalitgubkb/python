max = 3
data =[]

for i in range(max):
    num = int(input('Enter Your number %d:' %(i+1)))
    data = data +[num]
print('data = ',data)

print('Histogram')
for i in range(max):
    print('%5d %10d %s' %(i, data[i],'*'*data[i]))