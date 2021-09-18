from math import floor
from random import random
import matplotlib.pyplot as plt

def auto_scatter(func):
    def wrapper(*args, **kwargs):
        x, y = func(*args, **kwargs)
        plt.scatter(x, y)
        plt.show()
    return wrapper

@auto_scatter
def generate_random_points():
    x = [floor(random()*101) for _ in range(100)]
    y = [floor(random()*101) for _ in range(100)]

    return x, y

def main():
    generate_random_points()

if __name__ == "__main__":
    main()
