import math
from math import pi

age = 25  # 1
height = 5.10  # 2
complex_number = 2 + 3j  # 3

# 4
print('Area of the triangle')
base_input = input('Enter base: ')
height_input = input('Enter height: ')
area_of_triangle = (int(base_input) * int(height_input)) / 2
print(area_of_triangle)

# 5
print('Perimeter of the triangle')
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter_of_triangle = int(side_a) + int(side_b) + int(side_c)
print(perimeter_of_triangle)

# 6
print('Area and Perimeter of a rectangle')
length = input('Enter length: ')
width = input('Enter width: ')
area_of_rectangle = int(length) * int(width)
perimeter_of_rectangle = 2 * (int(length) + int(width))
print('The area of the rectangle is: ' + str(area_of_rectangle))
print('The perimeter of the rectangle is: ' + str(perimeter_of_rectangle))

# 7
r = float(input('Please input the radius: '))
area_of_circle = pi * r**2
circum_of_circle = 2 * pi * r
print('The area of the circle is: ' + str(area_of_circle))
print('The circumference of the circle is: ' + str(circum_of_circle))

# 8 - 11
slope = (10 - 2) / (6 - 2)
euc_dist = (math.dist([2, 2], [6, 10]))
print(slope)
print(euc_dist)
compare_slopes = slope - euc_dist
print(compare_slopes)

# 12
python_len = len('python')
dragon_len = len('dragon')
print(python_len != dragon_len)

#13
print('on' in 'python')
print('on' in 'dragon')

#14
print('jargon' in 'I hope this courseis not full of jargon')

#15


#16
print(type(str(float(len('python')))))

#17 if num % 2 == 0 then the number is even. ELSE the number is odd

#18
print(7 // 3 == 2.7)

#19
print('10' == 10)

#20
print(int(9.8) == 10)

#Q21
hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print('Your weekly earning is: ', hours * rate)

#Q22
years = int(input("Enter number of years you have lived: "))
print("You have lived for {} seconds".format(years*365*24*60*60))

#Q23
print(' \n 1 1 1 1 1 \n 2 1 2 4 8 \n 3 1 3 9 27 \n 4 1 4 16 64 \n 5 1 5 25 125')

