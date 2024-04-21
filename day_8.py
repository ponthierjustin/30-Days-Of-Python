# Justin
# 4/21/24

dog = {}

dog['name'] = 'Scooby'
dog['color'] = 'Brown'
dog['legs'] = 4
dog['age'] = 0

print(dog.get('name'))
print(dog.get('color'))
print(dog.get('legs'))
print(dog.get('age'))

student = {
    'first name': 'Justin',
    'last_name': 'Ponthier',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Java', 'HTML', 'Juggling'],
    'country': 'USA',
    'city': 'Roswell',
    'address': '123 Street Lane Roswell GA, 30076'
}

print(len(student))

print(student.get('skills'))

student['skills'].extend(['Rust', 'Go'])

print(student.get('skills'))

student_keys = print(student.keys())
student_values = print(student.values())
student_tuples = print(student.items())

student.pop('age')

print(student)

del dog