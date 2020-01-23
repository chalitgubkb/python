#วิธีการเขียนแบบ ธรรมดา

n1 = int(input('Enter Your Num 1: '))
n2 = int(input('Enter Your Num 2: '))

print(n1,'+',n2,'= %d' %(n1+n2))
print(n1,'-',n2,'= %d' %(n1-n2))
print(n1,'*',n2,'= %d' %(n1*n2))
print(n1,'/',n2,'= %d' %(n1/n2))



#วิธีการเขียนแบบ while
n = 1
o = []

while n<=2:
    i = int(input('Enter Your Number : '))
    o.append(i)
    n = n+1
print(o[0],'+',+o[1],'= %d' %(o[0]+o[1]))
print(o[0],'-',+o[1],'= %d' %(o[0]-o[1]))
print(o[0],'*',+o[1],'= %d' %(o[0]*o[1]))
print(o[0],'/',+o[1],'= %d' %(o[0]/o[1]))

