import datetime


# convert timestamp to datetime object
dt_object = datetime.datetime.now()

# get the hour and minute from the datetime object
hour = dt_object.hour
minute = dt_object.minute

if (12 <= hour < 13 and 1 <= minute <= 11) or (23 <= hour < 24 and 49 <= minute <= 59):
    print(1)
else:
    print(hour,minute)