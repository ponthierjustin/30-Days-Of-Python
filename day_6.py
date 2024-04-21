# Justin
# 4/21/24

empty_tuple = ()

brothers = ('Bradley', 'Bond', 'Adnan', 'Murtaza', 'Chase')

sisters = ('Jessica', 'Isabella', 'Brooklyn', 'Savannah')

siblings = brothers + sisters

print(len(siblings))

family_members = siblings + ('Dad', "Mom")

print(family_members)

siblings = family_members[0:9]
parents = family_members[-2:]

print(siblings)
print(parents)

fruits = ('banana', 'orange', 'mango')
vegetables = ('Asparagus', 'Cauliflower', 'Green Bean')
animals = ('Dog', 'Cat', 'Bunny')

food_stuff_tp = fruits + vegetables + animals

print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

middle_index = int(len(food_stuff_lt)/ 2) - 1
print(middle_index)
print(food_stuff_lt[middle_index])

print(food_stuff_lt[0:3])

print(food_stuff_lt[6:9])

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)