age = int(raw_input('Please enter your age: '))
if age < 18:
    print('')
    print('Sorry, you are too young!')
else:
    print('')
    print('You can enter!')
print('')
print ('OK, next, please pick three whole numbers, named x, y and z')
x = str(raw_input('x = '))
y = str(raw_input('y = '))
z = str(raw_input('z = '))
if x < y and x < z:
    print('x (' + x + ') is least!')
elif y < z:
    print('y (' + y + ') is least!')
else:
    print('z (' + z + ') is least!')
