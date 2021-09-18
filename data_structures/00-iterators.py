# An iterable is a structure that can be processed by a for loop.
my_list = [1, 2, 3, 4, 5] # An example, a list is an iterable
# You can transform iterables to iterators
my_iter = iter(my_list)
# And it can be traversed by:
print(next(my_iter)) # 1
print(next(my_iter)) # 2 
print(next(my_iter)) # 3

# Lets write a foor loop
my_list = ['Hello', 'World', 'I am not', 'a for loop']
for element in my_list:
    print(element)

# But for loops don't really exists, they are syntax sugar for 
my_list = ['Hello', 'World', 'I am not', 'a for loop']
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

print()

# You can create your own iterator with a class and the iterators protocol

class EvenNumber:
    """
    Class that implements iterators protocol with an inifinite 
    number of even numbers or smaller than a max number 
    """
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration
    def __len__(self):
        if self.max:
            return self.max+1
        else:
            return "Infinit"

even_list = EvenNumber(50)

for number in even_list:
    print(number)

print(len(even_list))