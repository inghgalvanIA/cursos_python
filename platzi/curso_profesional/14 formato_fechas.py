from datetime import datetime

my_datetime = datetime.now()

print(my_datetime)

my_str = my_datetime.strftime("%d/%m/%Y")
print(f"formato LATAM: {my_str}")

my_str = my_datetime.strftime("%m/%d/%Y")
print(f"formato USA: {my_str}")

my_str = my_datetime.strftime("Estamos en el año %Y")
print(f"formato año: {my_str}")