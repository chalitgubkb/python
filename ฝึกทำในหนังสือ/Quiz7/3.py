li = []
while True:
    l = int(input('Enter Number: '))
    if l == -1:
        break
    else:
        li.append(l)
mytuple = tuple(li)
print('list = ',type(mytuple))
print('Max = ',max(mytuple))
print('Min = ',min(mytuple))
print('Sum = ',sum(mytuple))