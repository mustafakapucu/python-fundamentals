from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time
# import datetime
# datetime.date

now = datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(datetime.ctime(now))
# print(datetime.strftime(now, '%Y'))
# print(datetime.strftime(now, '%X'))
# print(datetime.strftime(now, '%d'))
# print(datetime.strftime(now, '%A'))
# print(datetime.strftime(now, '%B'))
# print(datetime.strftime(now, '%Y %B %d'))

# t = '21 Nisan 2019'
# gun, ay, yil = t.split(' ')
# print(gun)

# t = '15 April 2019 hour 10:12:30'
# dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
# print(dt)
# print(dt.year)

birthday = datetime(2000, 5, 3, 12, 30, 5)
# print(birthday)

# print(datetime.timestamp(birthday)) # saniye bilgisi verir
# print(datetime.fromtimestamp(datetime.timestamp(birthday))) # saniye to datetime

timedeltaVal = now-birthday
print(timedeltaVal)  # timedelta
print(timedeltaVal.seconds)
print(now + timedelta(days=10))
print(now + timedelta(days=730, minutes=100))

print(now.year-10)