salary = float(input('Enter Yourด Salary : '))

if salary <= 20000:
    v = 2
    vat = (salary/100)*v
    print('Vat %d %% = %.2f' %(v,vat))
elif salary > 20000:
    v = 2.5
    vat = (salary/100)*v
    print('Vat %.2f %% = %.2f' %(v,vat))
