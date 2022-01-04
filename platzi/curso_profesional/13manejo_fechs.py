import datetime

#fecha completa
my_time = datetime.datetime.now()

print(my_time)

#dia fecha
my_day = datetime.date.today()

print(my_day)

#fecha por partes

print(f"año {my_day.year}")
print(f"mes {my_day.month}")
print(f"año {my_day.day}")