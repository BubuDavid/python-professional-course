# Generators are sugar syntax of iterators
# An example

def my_gen():
    """
    Generator example
    """
    print('Hello World!')
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n


    print("Hello hell!")
    n = 2
    yield n

a = my_gen()
print(next(a)) # Hello World!, 0
print(next(a)) # Hello heaven!, 1
print(next(a)) # Hello hell!, 2
#print(next(a)) # Stop Iteration exception
print()
# There exists generator comprehension like this
my_list = [0, 1, 4, 7, 9, 10]

my_second_list = [x*2 for x in my_list] # List comprehension
my_generator   = (x*2 for x in my_list) # Generator comprehension

for gen in my_generator:
    print(gen)