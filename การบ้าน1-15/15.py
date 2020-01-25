#เขียนแบบธรรมดา
n = 1
s = 0
while True:
    x = int(input('Enter Your Num : '))
    if x > s:
        s=x
    elif x==0:
        break
print('Max = ' , s)



#เขียนแบบ while เก็บค่าในอาเรย์
i = []
while True:
    n = int(input('Enter Your Number : '))
    i.append(n)
    if n == 0:
        break
print('Max = ',max(i))