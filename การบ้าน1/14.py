s = []
while True:
    n = int(input('Enter Your Number: '))
    s.append(n)
    if n == 0:
        break
print('Sum = ',sum(s))

#หรือแบบที่2
#sum = 0
#while True:
#    n = int(input('Enter Your Number: '))
#    sum = sum+n
#    if n == 0:
#        break
#print(sum)