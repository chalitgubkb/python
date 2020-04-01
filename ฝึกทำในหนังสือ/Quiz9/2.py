import os
os.system('cls')
os.system('color e')

filename = "province.txt"

f = open(filename, 'w')
text = "Phuket Phang-nga Krabi"
f.write('%s' %(text))
f.close()

fo = open(filename, 'r')
s = fo.read()
print(s)
fo.close()