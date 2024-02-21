import datetime

today = datetime.datetime.now()
today_without_microseconds = today.replace(microsecond=0)

print(today)
print(today_without_microseconds)