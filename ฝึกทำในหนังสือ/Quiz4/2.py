#เขียนค่าตามโจทย์
n = float(input('Enter Your Number : '))

if n < 5.0:
    print('Little or no damage')
elif 5.0 <= n and n < 5.5:
    print('Some damage')
elif 5.5 <= n and n < 6.5:
    print('Serious damage')
elif 6.5 <= n and n < 7.5:
    print('Disaster')
elif n >= 7.5:
    print('Catastrophe')

#เขียนไล่ค่าแบบช่วง
n = float(input('Enter Your Number : '))

if n < 5.0:
    print('Little or no damage')
elif n < 5.5:
    print('Some damage')
elif n < 6.5:
    print('Serious damage')
elif n < 7.5:
    print('Disaster')
elif n>= 7.5:
    print('Catastrophe')


