import random


def ph_no(number):
    p_no = []
    for i in range(number):
        d_1 = random.randint(7, 9)
        d_2 = random.randint(0, 9)
        d_3 = random.randint(0, 9)
        d_4 = random.randint(0, 9)
        d_5 = random.randint(0, 9)
        d_6 = random.randint(0, 9)
        d_7 = random.randint(0, 9)
        d_8 = random.randint(0, 9)
        d_9 = random.randint(0, 9)
        d_10 = random.randint(0, 9)
        unique_no = str(str(d_1) + str(d_2) + str(d_3) + str(d_4) + str(d_5) + str(d_6) +
                        str(d_7) + str(d_8) + str(d_9) + str(d_10))
        p_no.append(unique_no)
    return p_no


def phone_number():
    num = int(input("Enter the number of phone numbers you want: "))
    pno = ph_no(num)
    print(pno)
    return pno
