# Calculate the time a function takes to execute, and print the result using DECORATORS.

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        timeRes = func(*args)
        end = time.time()
        print("function exceuted in %0.6f seconds", end - start)
        return timeRes
    return wrapper

@timer
def func(val):
    time.sleep(val)
    
run = func(1)
        