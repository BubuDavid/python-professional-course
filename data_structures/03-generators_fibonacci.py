import time

def fibo_gen(max = None):
    n1, n2 = 0, 1
    counter = 0

    while not max or counter < max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield 1
        else:
            n1, n2 = n2, n1 + n2
            counter +=1
            yield n2


def main():
    fibonacci = fibo_gen(10)
    for fibo in fibonacci:
        print(fibo)
        time.sleep(0.06)

if __name__ == "__main__":
    main()