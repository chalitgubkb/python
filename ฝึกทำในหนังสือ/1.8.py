#วิธีการเขียนแบบ ธรรมดา
m1 = int(input('Enter Your Num: '))
m2 = int(input('Enter Your Num: '))

if m1 > m2:
    m = m1
    print('Max = ',m)
else:
    m = m2
    print('Max = ',m)



#วิธีการเขียนแบบ while

n1 = 1
ma = []
while n1 <= 2:
    i = int(input('Enter Your Num : '))
    ma.append(i)
    n1 = n1+1
print('Max = ',max(ma))
