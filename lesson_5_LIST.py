# СПИСОК
food = ["apple", "coconud", "banana"]
print(food)
print(food[0])
food[0] = "peach"
print(food)
food.append(True)
food.extend(["String", 2])
print(food)
food.remove(food[0])
print(food)
print("banana" in food)
print(food[::-1])