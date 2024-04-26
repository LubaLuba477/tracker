

from datetime import datetime
from datetime import timedelta

today = datetime.now().date()
# create a new datetime object , replacing the day , keep same everything else 
# - 
# using timedelta minus one day is always last months last day 
last_day_lastmonth = (today.replace(day=1) - timedelta(days=1))
first_day_lastmonth = last_day_lastmonth.replace(day=1)
print(first_day_lastmonth)
print(last_day_lastmonth)



# generate last three months 
mon3_first_day = (today.replace(day=1) - timedelta(days=55)).replace(day=1)
mon6_first_day = (today.replace(day=1) - timedelta(days=150)).replace(day=1)
year_first_day = today.replace(month=1 , day=1)
print("last 3", mon3_first_day, mon6_first_day, year_first_day)