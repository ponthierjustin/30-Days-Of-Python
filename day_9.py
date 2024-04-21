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