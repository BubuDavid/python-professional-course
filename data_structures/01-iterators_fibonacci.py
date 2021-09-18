import time

# We are going to create an iterator to build fibonacci numbers
# To print the firts n fibonacci numbers
class FiboIter():

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif self.max and self.counter >= self.max:
            raise StopIteration
        else:
            self.n1, self.n2 = self.n2, self.n1 + self.n2
            self.counter += 1
            return self.n2

def main():
    fibonacci = FiboIter(10)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)

if __name__ == "__main__":
    main()