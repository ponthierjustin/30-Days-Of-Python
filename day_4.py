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

# Q28
print(company.startswith('Coding'))
print(company.endswith('coding'))
