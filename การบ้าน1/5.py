P = float(input('Enter Your Product price: '))

vat = P*(7/100)
price = vat+P

print('Vat 7%% = %.2f\nSell price = %.2f' %(vat,price))