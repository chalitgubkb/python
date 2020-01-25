#โปรแกรมเก็บสถิติผลการเรียนวิชา introcom ของน.ศ ชั้นปีที่1จำนวณ100คนโดยรับค่าเกรดที่เป็นตัวอักษรจากน.ศ.แต่ละคน 
#แล้วนับว่ามีน.ศ. ที่ผ่าน(pass, เกรด A-D) น.ศ. ที่เรียนไม่ผ่าน(fail,เกรด E ) และ น.ศ. ที่ถอนรายวิชา(drop,เกรด w)
#แต่ละประเภทเป็นจำนวณเท่ามดบ้าง

A = []
B1 = []
B2 = []
C1 = []
C2 = []
D1 = []
D2 = []
E = []

p = 1
while p<=10:
    G = input('Enter Your Garde : ')
    if G == 'A':
        G=1
        A.append(G)
    elif G == 'B+':
        G=1
        B1.append(G)
    elif G == 'B':
        G=1
        B2.append(G)
    elif G == 'C+':
        G=1
        C1.append(G)
    elif G == 'C':
        G=1
        C2.append(G)
    elif G == 'D+':
        G=1
        D1.append(G)
    elif G == 'D':
        G=1
        D2.append(G)
    elif G == 'E':
        G=1
        E.append(G)
    p=p+1
print('-------------statistics-------------')
print('Garde A: %d Person' %(sum(A)))
print('Garde B+: %d Person' %(sum(B1)))
print('Garde B: %d Person' %(sum(B2)))
print('Garde C+: %d Person' %(sum(C1)))
print('Garde C: %d Person' %(sum(C2)))
print('Garde D+: %d Person' %(sum(D1)))
print('Garde D: %d Person' %(sum(D2)))
print('Garde E: %d Person' %(sum(E)))
print('-------------END-------------')
