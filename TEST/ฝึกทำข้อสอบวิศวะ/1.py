#จงเขียนโปรแกรมรับตัวเลขจำนวนเต็มจากแป้นพิมพ์เพียง1ค่า แล้วให้แสดงค่า factorial ของเลขจำนวนนั้น แสดงออกทางจอภาพ

f = 1
n = int(input('Enter Your NUM : '))
while n>=1:
   f = n*f
   n = n-1
print('Factorial = ',f)