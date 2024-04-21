# Justin
# 4/20/24

# Q1
empty_list = []

list_of_fruits = ['banana', 'orange', 'apple', 'pear', 'blueberry']

print(len(list_of_fruits))

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

it_companies[0] = 'Computacenter'
print(it_companies)

it_companies.append('Accenture')
print(it_companies)

it_companies.insert(4, 'Nvidia')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print('#; '.join(it_companies))

print('Apple' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3])

print(it_companies[6:9])

middle_index = int(len(it_companies)/ 2) - 1
print(middle_index)
print(it_companies[middle_index])

it_companies.remove(it_companies[0])
print(it_companies)

it_companies.remove(it_companies[middle_index])
print(it_companies)

it_companies.remove(it_companies[-1])
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

join_list = front_end + back_end

print(join_list)


full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)


