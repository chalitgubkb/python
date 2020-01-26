#ลิงค์โจทย์ https://sv1.picz.in.th/images/2020/01/26/RVkVL8.png
EH = []
EC = []
LH = []
LC = []
TH = []
TC = []
price = 0
alla = sum(EH+EC+LH+LC+TH+TC)
print('---BANANA CAFF---')
while True:
    p = input('\nEnter Your Price : ')
    if p == 'EH':
        price = 35
        EH.append(price)
        print('Buy',p,'=',alla,' baht')
    elif p == 'EC':
        price = 45
        EC.append(price)
        print('Buy',p,'=',sum(EH+EC+LH+LC+TH+TC),' baht')
    elif p == 'LH':
        price = 45
        LH.append(price)
        print('Buy',p,'=',sum(EH+EC+LH+LC+TH+TC),' baht')
    elif p == 'LC':
        price = 55
        LC.append(price)
        print('Buy',p,'=',sum(EH+EC+LH+LC+TH+TC),' baht')
    elif p == 'TH':
        price = 25
        TH.append(price)
        print('Buy',p,'=',sum(EH+EC+LH+LC+TH+TC),' baht')
    elif p == 'TC':
        price = 35
        TC.append(price)
        print('Buy',p,'=',sum(EH+EC+LH+LC+TH+TC),' baht')
    elif p == 'QQ':
        break
print('*------------------------*')
alla = sum(EH+EC+LH+LC+TH+TC)
r = float(input('\nEnter Reduce(%%) : '))
reducedprice = (alla/100)*r
re = alla-reducedprice
print('Reduce Price = %.2f Baht' %(re))
print('*------------END------------*')



