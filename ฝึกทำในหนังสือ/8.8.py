data = {
'Red':100,
'Green':200,
'Blue':300
}
print('data = ',data)

data2 = {
'Black':400,
'Yelllow':500
}
print('data2 = ',data2)
print('-'*50)
data2.update(data)
print('data = ',data)