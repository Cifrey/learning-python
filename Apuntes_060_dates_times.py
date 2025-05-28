
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'Spanish_Spain')

date = datetime.date(2025, 7, 9)
today = datetime.date.today() # module, class, method

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d/%m/%Y")

target_datetime = datetime.datetime(2025, 9, 7, 20, 54, 00)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

print(date)
print(today)
print(time)
print(now)

now = datetime.datetime.now()
now = now.strftime("%A, %d de %B de %Y a las %H:%M:%S") 
print(now)