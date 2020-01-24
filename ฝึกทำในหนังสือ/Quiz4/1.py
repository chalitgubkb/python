#เขียนแบบปกติ
M = int(input('Enter Month 1-12 : '))

if M == 1:
    print('January')
elif M == 2:
    print('February')
elif M == 3:
    print('March')
elif M == 4:
    print('April')
elif M == 5:
    print('May')
elif M == 6:
    print('June')
elif M == 7:
    print('July')
elif M == 8:
    print('August')
elif M == 9:
    print('September')
elif M == 10:
    print('October')
elif M == 11:
    print('November')
elif M == 12:
    print('December')
else:
    print('Error')

#หรือเขียนแบบดึงข้อมูลจากอาเรย์
mo = ['January','February','March','April','May','June','July','August','September','October','November','December']
M = int(input('Enter Month 1-12 : '))

if M == 1:
    print(mo[0])
elif M == 2:
    print(mo[1])
elif M == 3:
    print(mo[2])
elif M == 4:
    print(mo[3])
elif M == 5:
    print(mo[4])
elif M == 6:
    print(mo[5])
elif M == 7:
    print(mo[6])
elif M == 8:
    print(mo[7])
elif M == 9:
    print(mo[8])
elif M == 10:
    print(mo[9])
elif M == 11:
    print(mo[10])
elif M == 12:
    print(mo[11])
else:
    print('Error')