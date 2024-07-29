set_countries1 = {"Colombia", "Bolivia", "Mexico"}
set_countries2 = {"Peru", "Brazil", "Bolivia"}

# Union
set_union = set_countries1.union(set_countries2)
print(set_union)
print(set_countries1 | set_countries2)
set_union2 = set_countries1 | set_countries2
print(set_union2)

# Intersection
set_intersection = set_countries1.intersection(set_countries2)
print(set_intersection)
print(set_countries1 & set_countries2)
set_intersection2 = set_countries1 & set_countries2
print(set_intersection2)

# Difference
set_difference1 = set_countries1.difference(set_countries2)
print(set_difference1)
set_difference2 = set_countries2.difference(set_countries1)
print(set_difference2)

# Simetric difference
set_difference3 = set_countries1.symmetric_difference(set_countries2)
print(set_difference3)
print(set_countries1 ^ set_countries2)

names = {"Nicolas", "Miguel", "Juan", "Nicolas"}
print(names)
