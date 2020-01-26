#ลิงค์โจทย์ https://sv1.picz.in.th/images/2020/01/26/RVkVL8.png
EH = []
EC = []
LH = []
LC = []
TH = []
TC = []


print('---BANANA CAFF---')
while True:
    alla = sum(EH+EC+LH+LC+TH+TC)
    p = input('\nEnter Your Product Code : ')
    if p == 'EH':
        price = 35
        EH.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'EC':
        price = 45
        EC.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'LH':
        price = 45
        LH.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'LC':
        price = 55
        LC.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'TH':
        price = 25
        TH.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'TC':
        price = 35
        TC.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'QQ':
        break
print('*------------------------*')

print('\nPrice All = ',alla)
r = float(input('Enter Reduce % : '))
reducedprice = (alla/100)*r
print('Reduce -',r,'% = ',reducedprice)
re = alla-reducedprice
print('Reduce Price = %.2f Baht' %(re))
print('*------------END------------*')