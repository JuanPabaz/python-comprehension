original = [1, 2, 3, 4, 5]
new = []

for x in original:
    new.append(x * 2)

print(new)
new2 = list(map((lambda x: x * 2), original))
print(new2)

n = []
for i in range(1, 6):
    if i <= 2:
        n.append(i - 1)
print(n)
n2 = [i - 1 for i in range(1, 6) if i <= 2]
print(n2)


def sum(x, y):
    return x + y


print(sum(5, 6))

suma = lambda x, y: x + y
print(suma(5, 6))
