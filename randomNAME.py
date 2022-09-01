import random


def import_names(name_file):
    try:
        with open(name_file, 'r') as f_open:
            names = f_open.readlines()
            name_list = [x.strip().title() for x in names]
    except:
        print("name file not found\n")
    return name_list


def namegetter(firstnames, lastnames, count):
    names = []
    for i in range(0, count):
        first_name = random.choice(firstnames)
        last_name = random.choice(lastnames)
        rtn_name = first_name + ' ' + last_name
        names.append(rtn_name)
    return names


def generate_name(gender=None, count=1):
    gender_choices = ["M", "F"]

    first_names = []
    last_names = []
    if not gender or gender not in gender_choices:
        gender = random.choice(gender_choices)
    first_name_filename = f"names_{gender}.txt"
    first_names = import_names(first_name_filename)
    last_names = import_names("names_last.txt")

    return namegetter(first_names, last_names, count)

