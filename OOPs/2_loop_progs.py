# Exercise 1: Print first 10 natural numbers using while loop
def exercise_1():
    print("First 10 natural numbers using while loop:")
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()

# Exercise 2: Calculate the sum of all numbers from 1 to a given number
def exercise_2():
    num = int(input("Enter a number to calculate the sum of all numbers from 1 to that number: "))
    total_sum = sum(range(1, num + 1))
    print(f"The sum of all numbers from 1 to {num} is: {total_sum}")

# Exercise 3: Write a program to print multiplication table of a given number
def exercise_3():
    num = int(input("Enter a number to print its multiplication table: "))
    print(f"Multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Exercise 4: Display numbers from a list using loop
def exercise_4():
    numbers = [10, 20, 30, 40, 50]
    print("Numbers in the list:")
    for num in numbers:
        print(num, end=" ")
    print()

# Exercise 5: Count the total number of digits in a number
def exercise_5():
    num = int(input("Enter a number to count its digits: "))
    num_digits = len(str(abs(num)))  # Convert number to string and count digits
    print(f"The total number of digits in {num} is: {num_digits}")

# Exercise 6: Print list in reverse order using a loop
def exercise_6():
    numbers = [10, 20, 30, 40, 50]
    print("List in reverse order:")
    for num in reversed(numbers):
        print(num, end=" ")
    print()

# Exercise 7: Display numbers from -10 to -1 using for loop
def exercise_7():
    print("Numbers from -10 to -1:")
    for i in range(-10, 0):
        print(i, end=" ")
    print()

# Exercise 8: Use else block to display a message “Done” after successful execution of for loop
def exercise_8():
    print("Executing loop with else block:")
    for i in range(1, 6):
        print(i, end=" ")
    else:
        print("\nDone")

# Exercise 9: Write a program to display all prime numbers within a range
def exercise_9():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print()

# Exercise 10: Display Fibonacci series up to 10 terms
def exercise_10():
    print("Fibonacci series up to 10 terms:")
    a, b = 0, 1
    for _ in range(10):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Exercise 11: Find the factorial of a given number
def exercise_11():
    num = int(input("Enter a number to find its factorial: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

# Exercise 12: Reverse a given integer number
def exercise_12():
    num = int(input("Enter a number to reverse: "))
    reversed_num = 0
    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(f"The reversed number is: {reversed_num}")

# Exercise 13: Use a loop to display elements from a given list present at odd index positions
def exercise_13():
    numbers = [10, 20, 30, 40, 50, 60]
    print("Elements at odd index positions:")
    for i in range(1, len(numbers), 2):  # Start from index 1 and step by 2
        print(numbers[i], end=" ")
    print()

# Exercise 14: Calculate the cube of all numbers from 1 to a given number
def exercise_14():
    num = int(input("Enter a number to calculate the cube of all numbers from 1 to that number: "))
    print(f"Cubes of numbers from 1 to {num}:")
    for i in range(1, num + 1):
        print(f"{i}^3 = {i ** 3}")

# Exercise 15: Find the sum of the series up to n terms
def exercise_15():
    n = int(input("Enter the number of terms in the series: "))
    series_sum = sum(range(1, n + 1))
    print(f"The sum of the series from 1 to {n} is: {series_sum}")

def main():
    # Running all the exercises
    exercise_1()  # Exercise 1
    exercise_2()  # Exercise 2
    exercise_3()  # Exercise 3
    exercise_4()  # Exercise 4
    exercise_5()  # Exercise 5
    exercise_6()  # Exercise 6
    exercise_7()  # Exercise 7
    exercise_8()  # Exercise 8
    exercise_9()  # Exercise 9
    exercise_10()  # Exercise 10
    exercise_11()  # Exercise 11
    exercise_12()  # Exercise 12
    exercise_13()  # Exercise 13
    exercise_14()  # Exercise 14
    exercise_15()  # Exercise 15

main()