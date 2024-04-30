# Justin
# 4/23/2024

count = 0
while count < 11:
    print(count)
    count = count + 1

print('\n')

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for number in numbers:
    print(number)

print('\n')

numbers = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
for number in numbers:
    print(number)

print('\n')

count = 10
while count > 0:
    print(count)
    count = count - 1


count = 1 
for i in range(7):
    for i in range(count):
        print('#', end='')
    count += 1
    print('')

    for i in range(11):
        print(f"{i} x {i} = {i*i}")



frameworks_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in frameworks_list:
    print(item)


for i in range(0, 101, 2):
    print(i)


for i in range(1, 101, 2):
    print(i)

total = 0
for i in range(101):
    total += i

print("The sum of all numbers from 0 to 100 is:", total)

sum_even = 0
sum_odd = 0

for i in range(0, 101, 2):
    sum_even += i

for i in range(1, 101, 2):
    sum_odd += i

print("The sum of all even numbers from 0 to 100 is:", sum_even)
print("The sum of all odd numbers from 0 to 100 is:", sum_odd)





