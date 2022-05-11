

print("Lists")
friends = ["Kevin", "Smith", "Smith", "Smith", "Smith", "Smith"]
friends[3] = "Mike"
friends.sort()
print(friends)
lucky_numbers = [4, 5, 55, 66, 88]
lucky_numbers.reverse()

friends2 = friends.copy

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "jelly")
print(friends.index("Creed"))
print(friends.count("Smith"))
friends.remove(4)
lucky_numbers.clear()
friends.pop()


print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[3:4])

print(friends)
print(friends2)