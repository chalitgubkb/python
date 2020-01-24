#แบบแสดงค่าสูตรคูณแม่1-12ทันที โดยไม่มีรับค่าเพิ่ม
for n1 in range(2,12):
    for n2 in range(1,13):
        s = n1*n2
        print(n1,'X',n2,'= %d ' %(s))
    print('------------')
print('End')


#หรือเขียนแบบรับค่าเลื่อยๆไม่มีที่สิ้นสุด
while True:
    n1 = int(input('Enter Your Number: '))
    for n2 in range(1,13):
        s = n1*n2
        print(n1,'X',n2,'= %d ' %(s))
    print('------------')
print('End')
