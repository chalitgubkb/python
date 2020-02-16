#----------- ลูปรับค่าแบบ while ------------
i = 1
s = []
while i<=5:
    n = int(input('Enter Your Num :'))
    s.append(n)
    i = i+1
print('Min = %d' %(min(s)))
print('Max = %d' %(max(s)))

#--------------รับค่าแบบปกติ--------------

n1 = int(input('Enter Your N1 : '))
n2 = int(input('Enter Your N2 : '))
n3 = int(input('Enter Your N3 : '))
n4 = int(input('Enter Your N4 : '))
n5 = int(input('Enter Your N5 : '))

ss = (n1,n2,n3,n4,n5)

print(min(ss))
print(max(ss))
