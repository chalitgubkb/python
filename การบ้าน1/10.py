p = int(input('Enter Your Price: '))

if p >= 50000:
    v = 16
    vat = (p/100)*v+575
    print('Salary %d %% = %d ' %(v,vat))
elif p < 50000 and p >= 40000:
    v = 14
    vat = (p/100)*v+550
    print('Salary %d %% = %d ' %(v,vat))
elif p < 40000 and p >= 30000:
    v = 12
    vat = (p/100)*v+525
    print('Salary %d %% = %d ' %(v,vat))
elif p < 30000 and p >= 20000:
    v = 9
    vat = (p/100)*v+500
    print('Salary %d %% = %d ' %(v,vat))
elif p < 20000 and p >= 10000:
    v = 5
    vat = (p/100)*v+450
    print('Salary %d %% = %d ' %(v,vat))
elif p < 10000:
    v = 3
    vat = (p/100)*v+400
    print('Salary %d %% = %d ' %(v,vat))