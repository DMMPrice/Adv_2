import datetime


def name_break(n):
    for i in range(0, len(n)):
        if n[i] == ' ':
            return i


def ref_key(ad_no, name, dob):
    z = dob[3] + dob[4]
    datetime_object = datetime.datetime.strptime(z, "%m")
    m = datetime_object.strftime("%b")
    a = name_break(name)
    ref = name[0] + name[a + 1] + ad_no[0] + ad_no[4] + ad_no[8] + m + dob[0] + dob[1] + dob[6:]
    return ref.upper()
