#จงเขียนโปรแกรมตรวจสอบหาค่าต่ำสุดและค่าสูงสุด และหาค่าเฉลี่ย จากการรับค่าตัวเลขทศนิยม
# จำนวณ 10 ค่าจากผู้ใช้ และแสดงผลลัพิ์ที่ได้ทั้ง3ค่าออกทางจอภาพ

i = 1
m = []
while i <= 10:
    n = float(input('Enter Your Num : '))
    m.append(n)
    i = i+1

print('Max = %.2f' %(max(m)))
print('Min = %.2f' %(min(m)))
print('Avg = %.2f' %((sum(m)/10)))