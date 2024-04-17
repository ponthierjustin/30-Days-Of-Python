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

# 8 - 10
slope = (10 - 2) / (6 - 2)
euc_dist = (math.dist([2, 2], [6, 10]))
print(slope)
print(euc_dist)
compare_slopes = slope - euc_dist
print(compare_slopes)
