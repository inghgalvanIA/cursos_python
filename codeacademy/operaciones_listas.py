inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
first_3 = inventory[:3]
inventory_2_6 = inventory[2:6]
twin_beds = inventory.count('twin bed')
sort_inventory = inventory.sort()
print(inventory_len)
print(first)
print(last)
print(inventory_2_6 )
print(first_3)
print(twin_beds)
print(sort_inventory)