# Union
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
print(my_set1 | my_set2)
# {3, 4, 5, 6, 7}

# Intersection
print(my_set1 & my_set2)
# {5}

# Diff
print(my_set1 - my_set2)
# {3, 4}
print(my_set2 - my_set1)
# {6, 7}

# Symetric Difference
print(my_set1 ^ my_set2)
# {3, 4, 6, 7}
