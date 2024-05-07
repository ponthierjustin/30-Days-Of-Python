# 5/7/24
# Justin

from datetime import datetime
now = datetime.now()
print(now)                      
day = now.day                  
month = now.month               
year = now.year                
hour = now.hour               
minute = now.minute             
second = now.second
timestamp = now.timestamp()

print(f'{day}/{month}/{year}, {hour}:{minute}')  

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)



new_year = datetime(year=now.year + 1, month=1, day=1)
time_difference = new_year - now
print(f"Time difference to New Year: {time_difference}")

date_string_january = datetime(year=1970, month=1, day=1)
time_difference = now - date_string_january
print(f"Time difference from 1 January 1970 to now: {time_difference}")