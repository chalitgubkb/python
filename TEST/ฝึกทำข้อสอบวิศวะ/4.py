#เขียนโปรแกรมรับจำนวณวันทั้งหมดจากผู้ใช้ไปเลื่อยๆ แต่ละครั้งให้คำนวณเก็บเป็นข้อมูลว่าจากจำนวณวันที่รับมาคิดเป็นกี่ปีกี่เดือนกี่สัปดาห์ และ กี่วัน

month = 30
week  = 7
year = 365

while True:
    day = int(input('Enter Your Day : '))
    y = day/year
    m = day/month
    w = day/week
    print(day,'วัน = %d ปี'%y)
    print(day,'วัน = %d เดือน'%m)
    print(day,'วัน = %d สัปดาห์'%w)
    print('รวม = %d  วัน'%day)