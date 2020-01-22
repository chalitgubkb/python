i = []
while True:
    n = int(input('Enter Your Number : '))
    i.append(n)
    if n == 0:
        break
print('Max = ',max(i))