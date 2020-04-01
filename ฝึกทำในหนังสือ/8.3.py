data = {
'Red':100,
'Green':200,
'Blue':300,
400:'Black'
}

print('data = ',data)

print('Red in data = ','Red' in data)
print('Yellow in data','Yellow' in data)

print('Red not in data = ','Red' not in data)
print('Yellow not in data = ','Yellow' not in data)

print('-'*50)

del data[400]
print('data = ',data)
