# ---------
# Timezones
# ---------
# this code uses 'pytz timezone' to assign a specific timezone to a datetime object (.localize)
# then, the code converts the datetime object into a new one, with a different timezone (.astimezone)
# pytz accounts for time changes with daylight savings as shown below

# imports
import datetime
from pytz import timezone

# create datetime objects
myTime_1 = datetime.datetime.strptime("2019-01-17 08:00", "%Y-%m-%d %H:%M")
myTime_2 = datetime.datetime.strptime("2019-06-17 08:00", "%Y-%m-%d %H:%M")

# create timezones
usPacific = timezone('US/Pacific')
utc = timezone('UTC')

# assign timezones to datetime objects and store them as new variables
myTime1_usPacific = usPacific.localize(myTime_1)
myTime2_usPacific = usPacific.localize(myTime_2)

# use these new variables(with timezones assigned) and convert them to new UTC time
myTime1_utc = myTime1_usPacific.astimezone(utc)
myTime2_utc = myTime2_usPacific.astimezone(utc)

# print time in UTC
print("1) UTC:", myTime1_utc)
print("2) UTC:", myTime2_utc)

# print time in US/Pacific
print("1) US/Pacific:", myTime1_usPacific)
print("2) US/Pacific:", myTime2_usPacific)
