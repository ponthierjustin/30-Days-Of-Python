import math
#Testing code

fruits = ['banana', 'orange', 'mango', 'lemon']

input_fruits = input('Enter a fruit to the list: ')

if input_fruits not in fruits:
    fruits.append(input_fruits)
    print(fruits)
else:
    print('That fruit is already on the list!!!')