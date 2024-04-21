# Justin
# 4/21/24

user_age = int(input('Enter your age: '))
age_missing = str(18 - user_age)

print('You are old enough to learn to drive') if user_age >= 18 else print('You need ' +  age_missing + ' more years to learn to drive')
    
my_age = 26
your_age = int(input('Enter your age: '))
age_difference = str((your_age - my_age))
age_difference_2 = str((my_age - your_age))


if your_age > my_age:
    if age_difference == 1:
        print('We are 1 year apart')
    else:
        print('You are ' + age_difference + ' year older than me' )
else:
    print('I am ' + age_difference_2 + ' years older than you')


a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print('a is greater')
elif a > b:
    print('a is smaller than b')
else:
    print('a is equal to b')

grade = int(input('What grade did you receive?: '))

if grade >= 80:
    print('A')
elif grade >= 70 and grade <= 79:
    print('B')
elif grade >= 60 and grade <= 69:
    print('C')
elif grade >= 50 and grade <= 59:
    print('D')
else:
    print('F you FAIL')

month_input = input('What month is it?: ')
autumn = ['October', 'November', 'September']
winter = ['Decemeber', 'January', 'February']
summer = ['June', 'July', 'August']
spring = ['March', 'April', 'May']

if month_input in autumn:
    print('It is Autumn')
elif month_input in winter:
    print('It is Winter')
elif month_input in summer:
    print('It is Summer')
elif month_input in spring:
    print('It is spring')
else:
    print('That is not a valid month')


fruits = ['banana', 'orange', 'mango', 'lemon']

input_fruits = input('Enter a fruit to the list: ')

if input_fruits not in fruits:
    fruits.append(input_fruits)
    print(fruits)
else:
    print('That fruit is already on the list!!!')