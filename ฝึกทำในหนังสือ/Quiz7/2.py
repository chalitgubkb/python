li = []
while True:
    l = int(input('Enter Number: '))
    if l == -1:
        break
    else:
        li.append(l)
print('list = ',li)
print('Max = ',max(li))
print('Min = ',min(li))
print('Sum = ',sum(li))