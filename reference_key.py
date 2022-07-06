import datetime


def name_break(n):
    for i in range(0, len(n)):
        if n[i] == ' ':
            return i


def ref_key(ad_no, n, d):
    z = d[5] + d[6]
    datetime_object = datetime.datetime.strptime(z, "%m")
    m = datetime_object.strftime("%b")
    a = name_break(n)
    ref = n[0] + n[a + 1] + ad_no[0] + ad_no[4] + ad_no[8] + m + d[8] + d[9] + d[0:4]
    return ref.upper()
