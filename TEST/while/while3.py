#จงเขียนโปรแกรมคำนวณเกรด โดยรับคนมาก่อนว่ามีกี่คน แล้วนำเกรดของแต่ละคนมาคำนวณเกรด

grade = []

p = int(input('Enter Your Pepole : '))

while p > 0:
    g = int(input('Enter Grade : '))
    if g >= 80:
        grade.append('A')
    elif g >=70:
        grade.append('B')
    elif g >=60:
        grade.append('C')
    elif g >=50:
        grade.append('D')
    else:
        grade.append('E')
    
    p = p-1
print(grade)
