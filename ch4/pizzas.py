pizzas=['SCpizza','CQpizza','BJpizza']
for pizza in pizzas:
    print("I like " + pizza + " very much!")
print("I really like pizza!")

friend_pizzas=pizzas[:]
pizzas.append("TJpizza")
friend_pizzas.append("CDpizza")

print("My favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)