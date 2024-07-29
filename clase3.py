set_countries = {"Colombia", "Mexico", "Bolivia", "Colombia"}
print(len(set_countries))
print("Colombia" in set_countries)
print("Peru" in set_countries)

# Add
set_countries.add("Peru")
print(set_countries)
set_countries.add("Peru")
print(set_countries)

# Update
set_countries.update({"Venezuela", "Argentina", "Brazil", "Colombia"})
print(set_countries)

# Delete
set_countries.remove("Peru")
print(set_countries)
set_countries.discard("Colombia")  # Si no lo encuentra no saca error
print(set_countries)
set_countries.clear()  # Elimina todo el conjunto
print(set_countries)
print(len(set_countries))

original = [1, 2, 3, 4, 5]
new = []

for x in original:
    new.append(x * 2)

print(new)
new2 = list(map((lambda x: x * 2), original))
print(new2)
