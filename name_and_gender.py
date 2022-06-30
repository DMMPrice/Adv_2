import random
import indian_names as name


def name_and_gender():
    choice = random.randint(1, 2)
    name_gender = []
    if choice == 1:
        name_gender.append(name.get_full_name(gender='male'))
        name_gender.append("male")
    else:
        name_gender.append(name.get_full_name(gender='female'))
        name_gender.append("female")
    return name_gender
