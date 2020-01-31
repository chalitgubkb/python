#ลิงค์โจทย์  https://sv1.picz.in.th/images/2020/02/01/RFjqkN.png
name = input('Enter Your FullName: ')
MA = float(input('Enter Score Math : '))
TH = float(input('Enter Score Thai : '))
EN = float(input('Enter Score English : '))
DI = input('Enter Distance : ')
while True:
    SP = int(input('Enter Score Sport : '))
    if SP > 0:
        break
while True:
    MU = int(input('Enter Score Music : '))
    if MU > 0:
        break
AL = MA+TH+EN
spmu = (MU*2)+(MU*2)
SC = []
if AL < 100:
    AL = 1
    SC.append(AL)

elif AL >= 100 and AL<150:
    AL = 2
    SC.append(AL)

elif AL >= 150 and AL<200:
    AL = 4
    SC.append(AL)

elif AL >= 200 and AL<250:
    AL = 7
    SC.append(AL)

elif AL >= 250:
    AL = 10
    SC.append(AL)
    

if DI == 'A':
        DI = 4
        SC.append(DI)
        DI = 'A'
elif DI == 'B':
        DI = 3
        SC.append(DI)
        DI = 'B'
elif DI == 'C':
        DI = 2
        SC.append(DI)
        DI = 'C'
elif DI == 'D':
        DI = 1
        SC.append(DI)
        DI = 'D'

print('--------------------')
print('My Name = ',name)
print('Scouce Math+Thai+eng = ',AL)
print('Distance = ',DI)
print('Sport = ',SP)
print('Music = ',MU)
print('All Point = ',sum(SC)+spmu)
print('--------END-------')