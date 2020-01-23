#เขียนifelse ธรรมดา
n1 = int(input('Enter Your Nume1 : '))
n2 = int(input('Enter Your Nume1 : '))
if n1 > n2:
    print('Max = %d \n---End---' %(n1))
elif n2 > n1:
    print('Max = %d \n---End---' %(n2))


#เขียนแบบ while
m = []
i = 1
while i <=2:
    n = int(input('Enter Your Num : '))
    m.append(n)
    i = i+1
print('Max = %d \n---End---' %(max(m)))

#หากต้องการหาค่า min ก็แค่เปลี่ยนค่า maxเป็น min