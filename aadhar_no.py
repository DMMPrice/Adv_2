import random


# Function to create aadhar number where we have to enter starting value and ending value
def aadhar_no(starting_point, ending_point):
    uu_no = []
    for i in range(starting_point, ending_point, 1):
        digit_1 = random.randint(1, 9)
        digit_2 = random.randint(0, 9)
        digit_3 = random.randint(0, 9)
        digit_4 = random.randint(0, 9)
        digit_5 = random.randint(0, 9)
        digit_6 = random.randint(0, 9)
        digit_7 = random.randint(0, 9)
        digit_8 = random.randint(0, 9)
        digit_9 = random.randint(0, 9)
        digit_10 = random.randint(0, 9)
        digit_11 = random.randint(0, 9)
        digit_12 = random.randint(0, 9)
        unique_no = str(str(digit_1) + str(digit_2) + str(digit_3) + str(digit_4) + str(digit_5) + str(digit_6) + str(
            digit_7) + str(digit_8) + str(digit_9) + str(digit_10) + str(digit_11) + str(digit_12))
        uu_no.append(unique_no)
    deduplication(uu_no)
    return uu_no


# Function to remove the duplicate aadhar number from the aadhar list
def deduplication(test_list):
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    return res


if __name__ == '__main__':
    start = int(input("Enter the starting value: "))
    end = int(input("Enter the end value: "))
    uun = aadhar_no(start, end)
    for i in uun:
        print(i)
