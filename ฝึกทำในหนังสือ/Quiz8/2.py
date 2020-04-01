import os
os.system('cls')
os.system('color e')

def mydict():
    d = {}
    print("-"*20)
    d["Id"] = int(input('Enter ID : '))
    d["Title"] = str(input('Enter Title : '))
    d["Temp"] = float(input('Enter Temp : '))
    d["Humidity"] = int(input('Enter Humidity : '))
    os.system('cls')
    os.system('color a')

    print("-"*20)
    print('Id = ',d["Id"])
    print('Title = ',d["Title"])
    print('Temp = ',d["Temp"])
    print('Humidity = ',d["Humidity"])
    print("-"*20)

mydict()

#ผลลัพธ์จะได้
# --------------------
# Id =  804
# Title =  Phuket
# Temp =  27.8
# Humidity =  79
# --------------------