from math import pi

#Day 2: 30 Days of Python Programming \
first_name = 'Justin' 
last_name = 'Ponthier'  
full_name = 'Justin Ponthier' 
country = 'USA' 
city = 'Roswell' 
age = 25 
year = 2024 
is_married = False 
is_true = False 
is_light_on = False

car_make, car_model, car_year, car_color, is_car_on = 'Hyundai', 'Sonata', 2011, 'White', False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

first_name_length = len(first_name)
last_name_length = len(last_name)
print(first_name_length - last_name_length)

num_one = 5 
num_two = 4  

print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
print(num_one % num_two)
print(num_one ** num_two)
print(num_one // num_two)


r = float(input('Please input the radius: '))
area_of_circle = pi * r ** 2
circum_of_circle = 2 * pi * r
print('The area of the circle is: ' + str(area_of_circle))
print('The circumference of the circle is: ' + str(circum_of_circle))

first_name = input('What is your first name? ') 
last_name = input('What is your last name? ')    
country = input('What country do you live in? ')   
age = input('How old are you? ')  

print(first_name)
print(last_name)
print(first_name + ' ' + last_name)
print(country)
print(age)