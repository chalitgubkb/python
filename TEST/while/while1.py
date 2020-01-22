#รับค่าจากผู้ใช้5 ค่ามาก่อน แล้วแสดงเฉพาะเลขคี่ค่าที่รับมา โดยใช้ while
a = []
n = 1
while n <= 5:
    i = int(input('Enter Number : '))

    answer = i % 2
    if answer == 1:
     a.append(i)
    n = n+1

print(a)