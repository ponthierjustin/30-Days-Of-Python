# 5/8/24
# Justin

import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph.lower())  # Convert all words to lowercase
word_counts = Counter(words)

most_common_word, frequency = word_counts.most_common(1)[0]

print("Most frequent word:", most_common_word)
print("Frequency:", frequency)


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers = re.findall(r'-?\d+', text)
sorted_points = sorted(map(int, numbers))
distance = sorted_points[-1] - sorted_points[0]

print("Distance between the two furthest particles:", distance)



def is_valid_variable(variable):
    return bool(re.match(r'^[a-zA-Z_]\w*$', variable))

print(is_valid_variable('first_name'))  
print(is_valid_variable('first-name')) 
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = "I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher"

most_frequent_words = [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

print(cleaned_text)

print(most_frequent_words)