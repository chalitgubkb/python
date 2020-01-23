#แบบรับค่าเมื่อเจอเงื่อนไขจริงให้หยุดทำงาน
n = int(input('Enter Your Num : '))

if n >= 80:
    print('A')
elif n>=70:
    print('B')
elif n>=60:
    print('C')
elif n>=50:
    print('D')
elif n<50:
    print('E')

#แบบรับค่าไปเลื่อยๆ
i = 1
while i > 0:
    n = int(input('Enter Your Num : '))
    if n>=80:
        print('A')
    elif n>=70:
        print('B')
    elif n>=60:
        print('C')
    elif n>=50:
        print('D')
    elif n<50:
        print('E')
i = i+1
    