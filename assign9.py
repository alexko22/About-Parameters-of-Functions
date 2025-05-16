# Task 1: Writing Functions
def greet_user(name):
    print("Hello there", name, "You are a bold one!")
# Second function add_numbers...
def add_numbers(a, b):
    print(a, "+", b, "is", a+b)
    return a + b

# Task 2: Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print("I have a", animal_type, "named", pet_name)

# Task 3: Functions with Variable Arguments
def make_sandwhich(*args):
    print("Making a sandwhich with the following ingredients:", args)

# Task 4: Understanding Recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
# Now Fibonacci...
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        fibonacci(x-2) + fibonacci(x-1)
