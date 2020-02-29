data = ['January','February','March','April','May','June','July','August','September',
'October','November','December']
print('data = ',data)

print('len = ',len(data))

for i in range(0,len(data)):
    print('Month %d: %s ' %(i+1,data[i]))
