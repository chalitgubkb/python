import os
os.system('cls')
os.system('color e')

latest = open("latest.txt", 'r')
n = int(latest.read())

filename = "member.txt"
f = open(filename, 'a+',encoding='utf-8')
print('ถ้าจะออกจากโปรแกรมพิมพ์ bye ')
while True:
    member = input('ชื่อคนที่. %s. Enter Member:' %(n))
    if member =='bye':
            break
    f.write('ชื่อคนที่. %s. %s \n' %(n,member))
    n = n+1
    ls = open("latest.txt", 'w')
    ls.write('%s' %(n))

s = f.read()
os.system('cls')
print('-'*20)
fo = open(filename, 'r',encoding='utf-8')
s = fo.read()
print(s)
fo.close()
print('-'*20)
f.close()

#ผลลัพธ์จะได้
# ชื่อคนที่. 1. นาย งูหลาม รัดคอ 
# ชื่อคนที่. 2. นาย สมคิด คิดไม่ออก

#คำอธิบายเพิ่มเติม
#โปรแกรมจะloopรับค่าและบวกลำดับค่าเลื่อยๆจนกว่าจะinput คำว่า bye โปรแกรมจะหลุดออกจากloopแล้วแสดงผล
#encoding='utf-8 ทำให้สามารถinput ตัวอักขระได้ทั้งEngและThai
#ตัวแปร latest สร้างขึ้นมานอกเหนือจากโจทย์ เพื่อไว้สำหรับเก็บลำดับชื่อคนล่าสุด
  #เพื่อนำค่าล่าสุดมาloop ลำดับตัวเลข อีกครั้ง โดยจะสั่งให้เก็บค่าล่าสุดไว้ใน latest.txt