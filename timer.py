

'''Implement a decorator function called ‘timer’ that measures the execution time of a 
function. The ‘timer’ decorator should print the time taken by the decorated function to
 execute. Use the ‘time’ module in Python to calculate the execution time.'''


import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper

import time

@timer
def my_function():
    time.sleep(2)

my_function()
