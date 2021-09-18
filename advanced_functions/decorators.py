from datetime import date, datetime
from typing import Mapping

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        result = func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Passed ' + str(time_elapsed.total_seconds()) + " seconds")
        return result
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

# random_func()
print(sum(a=5,b=5))
