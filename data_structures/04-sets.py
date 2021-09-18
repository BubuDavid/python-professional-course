# Creating sets
my_set = {3, 4, 5}
print("my_set = ", my_set)

my_set2 = {"Hola", 23.3, False, True}
print("my_set2 = ", my_set2)

my_set3 = {3,3,2}
print("my_set3 = ", my_set3)

# my_set4 = {[1,2,3], 4}
# print("my_set4 = ", my_set4)

print()
# Casting to sets
my_list = [1,1,1,2,3,4,4,5]
my_set  = set(my_list)
print(my_set)
print()

# add an element
my_set.add(4)
print(my_set)
print()

# Add multiple elements
my_set.update([1, 2, 'hola'])
print(my_set)
print()

# Add multiples
my_set.update((1, 7, 2), {6, 8})
print(my_set)
print()
print('Remove:')

# Remove elements from sets
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 'hola'}
print(my_set)
print()

# Delete an existent element
my_set.discard(1)
print(my_set)
print()

# Delete an existent element
my_set.remove(2)
print(my_set)
print()


# Delete a unexistent element
my_set.discard(1000)
print(my_set)
print()


# Delete an unexistent element
my_set.remove(1000)
print(my_set)
print()
# ERRRRRROOOOORR