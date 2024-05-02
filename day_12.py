import random
import string

def generate_random_user_id():
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return random_id


user_id = generate_random_user_id()

print(user_id)
def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    user_ids = []
    for _ in range(num_ids):
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        user_ids.append(random_id)

    return user_ids

user_ids = user_id_gen_by_user()
print(user_ids)


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

color = rgb_color_gen()
print(f"RGB color: {color}")


def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        colors.append('#' + color)
    return colors

num_colors = 5
hex_colors = list_of_hexa_colors(num_colors)
print(hex_colors)

def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append((r, g, b))
    return colors

def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Invalid color type. Use 'hexa' or 'rgb'.")

num_colors = 5
hex_colors = generate_colors('hexa', num_colors)
rgb_colors = generate_colors('rgb', num_colors)

print("Hexadecimal colors:")
print(hex_colors)

print("\nRGB colors:")
print(rgb_colors)


def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

def random_unique_numbers():
    return random.sample(range(10), 7)

original_list = [1, 2, 3, 4, 5]
shuffled = shuffle_list(original_list)
print("Shuffled list:", shuffled)

random_numbers = random_unique_numbers()
print("Random unique numbers:", random_numbers)
