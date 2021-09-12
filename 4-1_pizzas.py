pizza_types = ['pepperoni pizza','pineapple pizza','sausage pizza','spicy-as-all-get-out pizza','dessert pizza']
for pizza in pizza_types:
    print(f"{pizza.capitalize()} is amazing and is real pizza, unlike other types of pizza.")
    print("If you want to be my friend, you must eat this pizza.\n")

print("Pizza is pretty great. And honestly, if you like any pizza we can still be friends. Even if you don't like real pizza.\n")

print(f"The first three items in the list are: {pizza_types[:3]}\n")
print(f"The middle three items in the list are: {pizza_types[1:4]}\n")
print(f"And finally, the last three items in the list are: {pizza_types[-3:]}\n")

friend_pizzas = pizza_types[:]

pizza_types.append('cheese pizza')
friend_pizzas.append('supreme pizza')

print("My favorite pizzas are:")
for pizza in pizza_types:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)