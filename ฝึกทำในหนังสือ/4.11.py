
#เขียนแบบรับค่า1ครั้งแล้วให้แสดง
i = 1
n = int(input('Enter Your Num : '))
while i <=12:
    s = n*i
    print(n,'X',i,'= %d ' %(s))
    i = i+1
print('---End---')


#หรือเขียนแบบรับค่าเลื่อนๆไม่มีสิ้นสุดแล้วให้แสดงแต่ละรอบ
while True:
    i = 1
    n = int(input('Enter Your Num : '))
    while i <=12:
        s = n*i
        print(n,'X',i,'= %d ' %(s))
        i=i+1
print('---End---')


