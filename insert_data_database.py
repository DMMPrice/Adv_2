import Phone_number
import aadhar_no as uid
import date_of_birth
import name_and_gender
import States_and_districts
import reference_key
import time
from faker import Faker
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'secure-connect-vault-labs.zip'
}
auth_provider = PlainTextAuthProvider('iQlsRObLADSowPtCiQxqPSTI',
                                      'HCk0xRq4Mx7cYCEQhJB6sd-nLOugKT5UZUfC4iQpluj411.g+pURyZzBxCbs8MyroBjjYC.ZuhvGHfoNBuSenY_kllukLC9-9en5mCYfDdFQ,ya69ZLfc9frXIhvbK4R')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('adv')
session.execute('USE adv')

fake = Faker()
# Name of the fields
fields = ['district', 'reference_key', 'id_no', 'address', 'dob', 'gender', 'name', "phone_no", 'states']
# This will create 1000 id numbers
id = uid.ad_no(1, 1000)

# This will create 1000 phone number
pno = Phone_number.ph_no(1000)

# Output File
# file = "Output/data2.csv"

for i in range(1, 500):
    # ini_time = time.time()

    # For the states
    states = States_and_districts.random_states()

    # Name of the district
    district = States_and_districts.random_districts(states)

    # For the id number
    id_no = id[i]

    # For the name
    name = fake.name()

    # For the dob
    dob = date_of_birth.date_of_birth()
    dob_remake = dob[6:] + '-' + dob[3:5] + '-' + dob[0:2]

    # For the reference key
    ref_key = str(reference_key.ref_key(str(id_no), str(name), str(dob)))

    # For the gender
    gender = name_and_gender.gender()

    # For the phone_no
    phone_no = int(pno[i])

    # For the address
    address = fake.address()

    # data = [district, ref_key, id_no, address, dob_remake, gender, name, states]
    # print(dob_remake)
    session.execute("""INSERT INTO adv(district, reference_key, id_no, address, dob, gender, phone_no,name, states)
                      VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        district, ref_key, id_no, address, dob_remake, gender, phone_no, name, states))
    print(i, "Data sent")
    time.sleep(2)
