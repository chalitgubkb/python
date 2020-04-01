import os
os.system('cls')
os.system('color e')

latest = open("latest.txt", 'r')
n = int(latest.read())

filename = "student.txt"
f = open(filename, 'a+',encoding='utf-8')
s = []
print('ถ้าจะออกจากโปรแกรมพิมพ์ bye ')
while True:
    if n == 3:
            break
    else:
        member = input('ชื่อคนที่ %s. Enter FullName: ' %(n+1))
        score = int(input('คะแนนคนที่. %s. Enter Score: ' %(n+1)))
        s.append(score)
        f.write('\nชื่อคนที่ %s. %s คะแนนสอบ = %s \n ' %(n+1,member,score))
        n = n+1

f.write('\nคะแนนสอบเฉลี่ยทั้ง %s คน = %d \n %s' %(n,(sum(s))/n,'-'*30))
ls = open("latest.txt", 'w')
ls.write('%s' %(n))
s = f.read()
os.system('cls')
fo = open(filename, 'r',encoding='utf-8')
s = fo.read()
print(s)
fo.close()
f.close()

#ผลลัพธ์จะได้
# ชื่อคนที่. 1. นาย งูหลาม รัดคอ  คะแนนสอบ = 10
# ชื่อคนที่. 2. นาย สมคิด คิดไม่ออก คะแนนสอบ = 20
# ชื่อคนที่. 3. นาง โควิด ไม่มีเขา คะแนนสอบ = 30
# คะแนนสอบเฉลี่ยทั้ง 3 คน = 20

#คำอธิบายเพิ่มเติม
# กำหนดให้ ตัวแปร latest ที่ อ้างอิงถึง ไฟล์ latest.txt = 0 เป็นค่าเริ่มต้น
# เพื่อ loop ลำดับคน เมื่อครบ3คน จะหลุด loop แล้วแสดงผล