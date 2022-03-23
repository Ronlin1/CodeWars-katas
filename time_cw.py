# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def sec_to_hours(seconds):
    HH = seconds//3600
    MM = (seconds%3600)//60
    SS = (seconds%3600)%60
    time = "{:02d}:{:02d}:{:02d}".format(HH, MM, SS)
    return time


# print(sec_to_hours(35999))

# Alternatives
def make_readable(n):
    return f'{n//3600:02d}:{(n%3600)//60:02d}:{n%60:02d}'

def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)

ef make_readable(n):
    return f'{n//3600:02d}:{(n%3600)//60:02d}:{n%60:02d}'