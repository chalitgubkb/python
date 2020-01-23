#เขียนแบบปกติifelse
n = int(input('Enter Your Score : '))
if n >=80:
    print('Grade: A')
elif n >=60:
    print('Grade: B')
elif n >=60:
    print('Grade: C')
elif n >=50:
    print('Grade: D')
elif n <=49:
    print('Grade: E')

#หรือเขียนแบบดึงข้อมูลจาก listอาเรย์
G = ['Grade: A','Grade: B','Grade: C','Grade: D','Grade: E']
n = int(input('Enter Your Score : '))
if n >=80:
    print(G[0])
elif n >=60:
    print(G[1])
elif n >=60:
    print(G[2])
elif n >=50:
    print(G[3])
elif n <=49:
    print(G[4])

