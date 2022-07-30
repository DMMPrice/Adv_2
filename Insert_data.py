import base64
import csv
import Phone_number
import aadhar_no as uid
import date_of_birth
import name_and_gender
import States_and_districts
import reference_key
import time
from faker import Faker

fake = Faker()
# Name of the fields
fields = ['district', 'reference_key', 'id_no', 'address', 'dob', 'gender', 'name', 'states']
# This will create 1000 id numbers
id = uid.ad_no(1, 1000)

# This will create 1000 phone number
pno = Phone_number.ph_no(1000)

# Output File
file = "Output/data2.csv"

# Data rows of the csv file
with open(file, "w+") as f:
    write = csv.writer(f)
    write.writerow(fields)
    for i in range(1, 500):
        ini_time = time.time()

        # For the states
        states = States_and_districts.random_states()

        # Name of the district
        district = States_and_districts.random_districts(states)

        # For the id number
        id_no = int(id[i])

        # For the name
        name = fake.name()

        # For the dob
        dob = date_of_birth.date_of_birth()
        dob_remake = dob[6:] + '-' + dob[3:5] + '-' + dob[0:2]

        # For the reference key
        ref_key = reference_key.ref_key(str(id_no), str(name), str(dob))

        # For the gender
        gender = name_and_gender.gender()

        # For the phone_no
        phone_no = int(pno[i])

        # For the address
        address = fake.address()

        # # For the 512 iris code
        # parent_path = 'C:/Docs/Data Vault/DV/generated/'
        # with open(parent_path + str(i) + '/' + '1_mask.txt', "rb") as f:
        #     read = f.read()
        #     f.close()
        # iris_code = base64.b16encode(read)
        #
        # # For the 10 fingerprint
        # fig = 10 * i
        # fingerprint = []
        # for fig_1 in range(fig - 9, fig + 1):
        #     fig_path = "C:/Docs/Data Vault/DV/1K/"
        #     with open(fig_path + str(fig_1) + '.jpg', 'rb') as f:
        #         data = base64.b64encode(f.read())
        #         fingerprint.append(str(data))
        #         f.close()
        #
        # # For the profile picture
        # profile_pic_path = "C:/Docs/Data Vault/DV/Profile_pic_1/Profile_pic_1/"
        # with open(profile_pic_path + str(i) + '.jpg', "rb") as f:
        #     read = f.read()
        #     data = base64.b64decode(read)
        #     f.close()

        data = [district, ref_key, id_no, address, dob_remake, gender, name, states]
        write.writerow(data)
        print(i, 'data sent')
        print('Time taken', time.time() - ini_time)
