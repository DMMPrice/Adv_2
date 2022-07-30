import random

year = []
for i in range(1927, 2023):
    year.append(i)


def is_leap(year_of_birth):
    if (year_of_birth % 400 == 0) and (year_of_birth % 100 == 0):
        return ['leap', str(year_of_birth)]

    elif (year_of_birth % 4 == 0) and (year_of_birth % 100 != 0):
        return ['leap', str(year_of_birth)]
    else:
        return ['not leap', str(year_of_birth)]


def leap_year_date(month_no):
    if month_no % 2 == 0:
        return random.randint(1, 28)
    if month_no == 2:
        return random.randint(1, 28)
    else:
        return random.randint(1, 30)


def not_leap_year_date(month_no):
    if month_no % 2 == 0:
        return random.randint(1, 28)
    if month_no == 2:
        return random.randint(1, 28)
    else:
        return random.randint(1, 30)


def date_of_birth():
    global year
    year_of_birth = year[random.randint(0, len(year) - 1)]
    year_of_birth_check = is_leap(year_of_birth)
    month = random.randint(1, 12)
    if year_of_birth_check[0] == 'leap':
        date = leap_year_date(month)
        if month < 10:
            month = '0' + str(month)
        if date < 10:
            date = '0' + str(date)
        dob = str(date) + '-' + str(month) + '-' + str(year_of_birth_check[1])
        return dob
    if year_of_birth_check[0] == 'not leap':
        date = leap_year_date(month)
        if month < 10:
            month = '0' + str(month)
        if date < 10:
            date = '0' + str(date)
        dob = str(date) + '-' + str(month) + '-' + str(year_of_birth_check[1])
        return dob
