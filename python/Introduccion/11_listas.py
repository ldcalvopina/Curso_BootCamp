lenguajes = ["Python", "c++", "go", "Javascript"]
#print(type(lenguajes))

print(lenguajes)
print(lenguajes[3])
lenguajes[2]="Html"
print(lenguajes[1:4])
print(lenguajes[:4])
print(lenguajes[1:])

#lenguajes = ["Python", 1, 22.25, ["a", "b", "c"], "go", "Javascript"]
#print(lenguajes)

lenguajes.insert(2, "Css")
print(lenguajes)

lenguajes.remove(lenguajes[2])
print(lenguajes)

print("php" in lenguajes)

print(len(lenguajes))

