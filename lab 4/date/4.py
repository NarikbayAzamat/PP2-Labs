import datetime

def date_difference(date1, date2):
    difference = date2 - date1
    difference_in_sec = difference.total_seconds()

    return difference_in_sec

date1 = datetime.datetime(2024, 2, 11, 12, 0, 0)
date2 = datetime.datetime(2024, 2, 17, 15, 30, 0)

print(date_difference(date1, date2))