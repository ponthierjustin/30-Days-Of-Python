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

