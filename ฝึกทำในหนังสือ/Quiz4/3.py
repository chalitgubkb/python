name = input('Enter Your Name : ')
salary = int(input('Enter Your Salary : '))
OT = int(input('Enter Your OT : '))

s = salary+OT

if s>=100000:
    vat = 10
    print('MyName ',name,'\nSalary = ',salary,'\nOT = ',OT)
    print('vat',vat,'%% = %d' %((s/100)*vat))
elif s>=70000:
    vat = 7
    print('MyName ',name,'\nSalary = ',salary,'\nOT = ',OT)
    print('vat',vat,'%% = %d' %((s/100)*vat))
elif s>=50000:
    vat = 5
    print('MyName ',name,'\nSalary = ',salary,'\nOT = ',OT)
    print('vat',vat,'%% = %d' %((s/100)*vat))
elif s>=30000:
    vat = 3
    print('MyName ',name,'\nSalary = ',salary,'\nOT = ',OT)
    print('vat',vat,'%% = %d' %((s/100)*vat))
elif s<30000:
    vat = 1
    print('MyName ',name,'\nSalary = ',salary,'\nOT = ',OT)
    print('vat',vat,'%% = %d' %((s/100)*vat))
