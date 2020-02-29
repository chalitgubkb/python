data = []

while True:
    num=int(input('Enter Your number:'))
    if(num<0):
        break
    data += [num]
print('-'*50)
print('data = ',data)

print('Max = ',max(data))
print('Min = ',min(data))
print('Sum = ',sum(data))