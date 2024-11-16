first = int(input('Print the first number: '))
second = int(input('Print the second number: '))
third = int(input('Print the third number: '))

if first == second == third:
    print('All numbers are equal: 3')
elif first == second or first == third or second == third:
    print('Just two is equal: 2')
else:
    print('Numbers are not equal: 0')
