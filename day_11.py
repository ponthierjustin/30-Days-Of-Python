import math

def add_two_numbers(a, b):
    return a + b

def area_of_circle(radius):
    return math.pi * radius * radius

def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Please provide only numbers in the list."

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real roots"

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(arr):
    return arr[::-1]

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(1, n+1))
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)
def evens_and_odds(n):
    evens = sum(1 for digit in str(n) if int(digit) % 2 == 0)
    odds = sum(1 for digit in str(n) if int(digit) % 2 != 0)
    return evens, odds


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_empty(value):
    return not bool(value)

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

def calculate_mode(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    max_freq = max(freq.values())
    return [item for item, freq in freq.items() if freq == max_freq]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return calculate_variance(lst) ** 0.5

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def are_items_unique(lst):
    return len(lst) == len(set(lst))

def are_items_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

def is_valid_variable(variable):
    import re
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None

def most_spoken_languages():
    from data.countries_data import countries
    languages = {}
    for country in countries:
        for language in country['languages']:
            if language in languages:
                languages[language] += country['population']
            else:
                languages[language] = country['population']
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return [language for language, population in sorted_languages][:10]

def most_populated_countries():
    from data.countries_data import countries
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [country['name'] for country in sorted_countries][:10]

print(add_two_numbers(3, 5))  # Output: 8
print(area_of_circle(5))       # Output: 78.53981633974483
print(add_all_nums(1, 2, 3, 4))# Output: 10
print(convert_celsius_to_fahrenheit(25))  # Output: 77.0
print(check_season(3))         # Output: Spring
print(calculate_slope(0, 0, 1, 1))        # Output: 1.0
print(solve_quadratic_eqn(1, -3, 2))       # Output: (2.0, 1.0)
print_list([1, 2, 3, 4, 5])    # Output: 1 2 3 4 5
print(reverse_list([1, 2, 3, 4, 5]))      # Output: [5, 4, 3, 2, 1]
my_list = ["apple", "banana", "cherry"]
print(capitalize_list_items(my_list))  # Output: ['Apple', 'Banana', 'Cherry']

new_list = add_item(my_list, "date")
print(new_list)  # Output: ['apple', 'banana', 'cherry', 'date']
my_list = ["apple", "banana", "cherry"]
new_list = remove_item(my_list, "banana")
print(new_list)  # Output: ['apple', 'cherry']
print(sum_of_numbers(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)
print(sum_of_odds(5))   # Output: 9 (1 + 3 + 5)
print(sum_of_even(5))   # Output: 6 (2 + 4)
evens, odds = evens_and_odds(123456)
print("Number of evens:", evens)   # Output: 3
print("Number of odds:", odds)     # Output: 3
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(factorial(5))               # Output: 120
print(is_empty(num_list))         # Output: False
print(calculate_mean(num_list))   # Output: 5.5
print(calculate_median(num_list)) # Output: 5.5
print(calculate_mode(num_list))   # Output: []
print(calculate_range(num_list))  # Output: 9
print(calculate_variance(num_list)) # Output: 8.25
print(calculate_std(num_list))    # Output: 2.8722813232690143
print("Is 7 prime?", is_prime(7))  # Output: True
print("Are items unique?", are_items_unique([1, 2, 3, 4, 5]))  # Output: True
print("Are items of same type?", are_items_same_type([1, 2, 3]))  # Output: True
print("Is 'my_variable' a valid variable name?", is_valid_variable('my_variable'))  # Output: True


