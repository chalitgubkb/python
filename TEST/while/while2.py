#รับค่าจากผู้ใช้10 ค่ามาก่อน แล้วนำค่าทั้งหมดมารวมกันโดยใช้ while
s = []
n = 1
sum = 0

while n <= 2:
    number = int(input('Enter Num : '))
    s.append(number) #เอาค่า number ไปเก็บไว้ใน s โดยใช้ append
    sum = sum + s[n - 1]
    n = n + 1
print('List : ',s)
print('sum = ',sum)