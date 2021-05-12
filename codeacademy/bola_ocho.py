import random
                                       
name = input("¿cual es tu nombre?")
question = input("¿cual es tu pregunta?")
list1 = [1, 2, 3, 4, 5, 6]

num_ran = random.choice(list1)
print(num_ran)

if num_ran == 1:
    print("puede ser")
elif num_ran == 2:
    print("No")
elif num_ran == 3:
    print("Si")
elif num_ran == 4:
    print("No te rindas sigue intendandolo")
elif num_ran == 5:
    print("Vuelve a intentar")
elif num_ran == 6:
    print("Parece que no")
else:
    print("Error")