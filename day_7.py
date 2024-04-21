# Justin    
# 4/21/24

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]



print(len(it_companies))

it_companies.add('Twitter')

print(it_companies)

it_companies.update(['Computacenter', 'Accenture', 'Nvidia'])

print(it_companies)

it_companies.remove('Nvidia')

print(it_companies)

#Discard will not raise an error even if the item is not found

a_b = A.union(B)

print(a_b)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

b_a = B.union(A)

print(b_a)

print(A.symmetric_difference(B))

del a_b
del b_a
del A
del B

age_set = set(age)

print(len(age))
print(len(age_set))
# List is bigger

# String: A collection of one or more characters under a single or double quote.
# List: Python list is an ordered collection which allows to store different data type items. 
# Tuple: A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created.
# Set: A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items

teacher = 'I am a teacher and I love to inspire and teach people.'

teacher_list = teacher.split(' ')

teacher_set = set(teacher_list)

print(teacher_set)
