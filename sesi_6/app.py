# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'


# my_generator()

# for char in my_generator():
#     print(char)

# def counter_generator(low, high):
#     while low <= high:
#         yield low
#         low += 1


# object_gen = counter_generator(5, 10)
# print(next(object_gen))
# print(next(object_gen))
# print(next(object_gen))
# print(next(object_gen))


# def say_hello(name):
#     return f"Hello {name}"


# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"


# def greet_bob(greeter_func):
#     return greeter_func("Bob")


# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()


# parent()

# def parent(num=0):
#     def first_child():
#         return "Hi, I am Bayu"

#     def second_child():
#         return "Call me Nurmansah"

#     if num == 1:
#         return first_child
#     else:
#         return second_child


# first = parent(1)
# print(first())

# def bay(num):
#     return num


# def bay():
#     return 'x'


# d = bay(1)
# print(d)

import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)
waste_some_time(999)
