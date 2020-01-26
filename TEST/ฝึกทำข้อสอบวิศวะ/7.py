text = []
f = []
c = input('Enter Your Char : ')
text.append(c)
print('Ouput = ',c)
print(len(c))

f = input('Enter Your TextFind : ')
print(text.count(f))

c2 = input('Enter Your Char2 : ')
print(text.replace(c2))