
def n():
        g = float(input('Enter Grade: '))
        return g

def avg():
    while True:
        b=n()
        if b >= 80 and b <= 100:
            print('A')
            break
        elif b >= 70 and b <= 79:
            print('B')
            break
        elif b >= 60 and b <= 69:
            print('C')
            break
        elif b >= 50 and b <= 59:
            print('D')
            break
        elif b >=0 and b <= 49:
            print('E')
            break
avg()