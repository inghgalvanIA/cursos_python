toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
pizzas = list(zip(toppings,prices))
sort_pizza = pizzas.sort()

print(toppings)
print(prices)
print(num_pizzas)
print(f"We sell {num_pizzas} different kinds of pizza!")
print(pizzas)
print("################################")
print(sort_pizza)
