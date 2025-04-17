# Exercise 1: Create a function in Python
def exercise_1():
    def greet():
        print("Hello! This is a simple function.")
    greet()

# Exercise 2: Create a function with variable length of arguments
def exercise_2():
    def sum_numbers(*args):
        total = sum(args)
        print(f"The sum of the numbers is: {total}")
    
    sum_numbers(1, 2, 3, 4, 5)  # Example with 5 numbers
    sum_numbers(10, 20)  # Example with 2 numbers

# Exercise 3: Return multiple values from a function
def exercise_3():
    def get_coordinates():
        return 10, 20  # Returning multiple values as a tuple
    
    x, y = get_coordinates()  # Unpacking the returned tuple
    print(f"The coordinates are: x = {x}, y = {y}")

# Exercise 4: Create a function with a default argument
def exercise_4():
    def greet(name="Guest"):
        print(f"Hello, {name}!")
    
    greet()  # Uses default argument
    greet("Alice")  # Uses custom argument

# Exercise 5: Create an inner function to calculate the addition
def exercise_5():
    def outer_function(a, b):
        def inner_function(x, y):
            return x + y
        return inner_function(a, b)
    
    result = outer_function(10, 20)
    print(f"The sum inside the inner function is: {result}")

# Exercise 6: Create a recursive function
def exercise_6():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    
    num = 5
    print(f"The factorial of {num} is: {factorial(num)}")

# Exercise 7: Assign a different name to function and call it through the new name
def exercise_7():
    def original_function():
        print("This is the original function.")
    
    new_name_for_function = original_function  # Assigning a new name
    new_name_for_function()  # Calling the function using the new name

def main():
    exercise_1()  # Exercise 1
    exercise_2()  # Exercise 2
    exercise_3()  # Exercise 3
    exercise_4()  # Exercise 4
    exercise_5()  # Exercise 5
    exercise_6()  # Exercise 6
    exercise_7()  # Exercise 7

main()