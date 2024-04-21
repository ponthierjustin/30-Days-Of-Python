# Justin
# 4/18/24

# Q1
thirty_days_of_python_string = ['Thirty', 'Days', 'Of', 'Pyhton']
result = ' '.join(thirty_days_of_python_string)
print(result)

# Q2
coding_for_all_string = ['Coding', 'For', 'All']
result = ' '.join(coding_for_all_string)
print(result)

# Q3
company = 'Coding For All' 

# Q4
print(company)

# Q5
print(len(company))

# Q6
print(company.upper())

# Q7
print(company.lower())

# Q8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Q9
first_word_slice = company[7:]
print(first_word_slice)

# Q10
print(company.find('Coding'))

# Q11 # Q12
print(company.replace('Coding', "Python").replace('All', 'Everyone'))

# Q13
print(company.split(' '))

# Q14
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

# Q15
print(company[0])

# Q16 
print(company[-1])

# Q17
print(company[10])

# Q18 - 19
'AFE'
'CFA'

# Q20 - 22
print(company.find('C'))
print(company.find('F'))
print(company.rfind('i'))

# Q23 - 27
practice = 'You cannot end a sentence with because because because is a conjunction'
print(practice.index('because'))
print(practice.rfind('because'))
print(practice[31:54])

# Q28 - 29
print(company.startswith('Coding'))
print(company.endswith('coding'))

# Q30
print('   Coding For All      '.strip(' '))

# Q31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Q32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# Q33
print('I am enjoying this challenge. \nI just wonder what is next. \n')

# Q34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki\n') 

# Q35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.\n'.format(radius, area))

# Q36
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))