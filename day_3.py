age = 25
height = 5.10
complex_number = 2 + 3j

print('Area of the triangle')
base_input = input('Enter base: ')
height_input = input('Enter height: ')
area_of_triangle = (int(base_input) * int(height_input)) / 2
print(area_of_triangle)

print('Perimeter of the triangle')
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter_of_triangle = int(side_a) + int(side_b) + int(side_c)
print(perimeter_of_triangle)

print('Area and Perimeter of a rectangle')
length = input('Enter length: ')
width = input('Enter width: ')
area_of_rectangle = int(length) * int(width)
perimeter_of_rectangle = 2 * (int(length) + int(width))
print('The area of the rectangle is: ' + str(area_of_rectangle))
print('The perimeter of the rectangle is: ' + str(perimeter_of_rectangle))
