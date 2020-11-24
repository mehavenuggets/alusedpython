fruits = ["Arbuus",  "Banaan", "Pomelo"]
print(fruits)
print(fruits[0])
fruits.append("Maasikas")
print(fruits[3])
fruits[1] = "Sidrun"
print(fruits)
if "Arbuus" in fruits:
    print("Arbuus on listis")
else:
    print("Arbuus ei ole listis")
print(len(fruits))
fruits.remove("Arbuus")
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)