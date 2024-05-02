numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)


list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print(flattened_list)


result = [(i,) + tuple([j**i for j in range(7)]) for i in range(11)]

for tup in result:
    print(tup)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

print(output)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

print(output)
