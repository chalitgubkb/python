#แบบไม่ส่งค่ากลับ
def c():
    Fahrenheit = float(input('Enter Your °F : '))
    Celsius = (5/9)*(Fahrenheit-32)
    print('°F Convert °C = %.2f' %(Celsius))
c()

#===================================================

#แบบส่งค่ากลับ
def cc(F):
    Celsius = (5/9)*(Fahrenheit-32)
    print('°F Convert °C = %.2f' %(Celsius))
Fahrenheit = float(input('Enter Your °F : '))
cc(Fahrenheit)