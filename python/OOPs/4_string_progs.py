# Exercise 1: Create a string made of the first, middle and last character
def exercise_1():
    def first_middle_last(s):
        first = s[0]
        middle = s[len(s)//2] if len(s) % 2 != 0 else ""
        last = s[-1]
        return first + middle + last

    input_str = input("Enter a string: ")
    result = first_middle_last(input_str)
    print(f"String made of first, middle, and last character: {result}")

# Exercise 2: Append new string in the middle of a given string
def exercise_2():
    def append_middle(s, new_str):
        middle = len(s) // 2
        return s[:middle] + new_str + s[middle:]

    input_str = input("Enter a string: ")
    new_str = input("Enter a string to append in the middle: ")
    result = append_middle(input_str, new_str)
    print(f"String after appending in the middle: {result}")

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
def exercise_3():
    def create_new_string(s):
        first = s[0]
        middle = s[len(s)//2] if len(s) % 2 != 0 else ""
        last = s[-1]
        return first + middle + last

    input_str = input("Enter a string: ")
    result = create_new_string(input_str)
    print(f"New string made of first, middle, and last characters: {result}")

# Exercise 4: Arrange string characters such that lowercase letters should come first
def exercise_4():
    def arrange_lowercase_first(s):
        lower = ''.join([char for char in s if char.islower()])
        upper = ''.join([char for char in s if char.isupper()])
        return lower + upper

    input_str = input("Enter a string: ")
    result = arrange_lowercase_first(input_str)
    print(f"String with lowercase letters first: {result}")

# Exercise 5: Count all letters, digits, and special symbols from a given string
def exercise_5():
    def count_characters(s):
        letters = sum(1 for char in s if char.isalpha())
        digits = sum(1 for char in s if char.isdigit())
        special = sum(1 for char in s if not char.isalnum())
        return letters, digits, special

    input_str = input("Enter a string: ")
    letters, digits, special = count_characters(input_str)
    print(f"Letters: {letters}, Digits: {digits}, Special symbols: {special}")

# Exercise 6: String characters balance Test
def exercise_6():
    def is_balanced(s):
        return s == s[::-1]

    input_str = input("Enter a string: ")
    if is_balanced(input_str):
        print(f"The string '{input_str}' is balanced (Palindrome).")
    else:
        print(f"The string '{input_str}' is not balanced.")

# Exercise 7: Find all occurrences of a substring in a given string by ignoring the case
def exercise_7():
    def find_occurrences(s, sub):
        return s.lower().count(sub.lower())

    input_str = input("Enter the main string: ")
    sub_str = input("Enter the substring to search for: ")
    count = find_occurrences(input_str, sub_str)
    print(f"The substring '{sub_str}' appears {count} times in the string.")

# Exercise 8: Calculate the sum and average of the digits present in a string
def exercise_8():
    def sum_and_average_of_digits(s):
        digits = [int(char) for char in s if char.isdigit()]
        total_sum = sum(digits)
        average = total_sum / len(digits) if digits else 0
        return total_sum, average

    input_str = input("Enter a string: ")
    total_sum, average = sum_and_average_of_digits(input_str)
    print(f"Sum of digits: {total_sum}, Average of digits: {average}")

# Exercise 9: Write a program to count occurrences of all characters within a string
def exercise_9():
    def count_characters_frequency(s):
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    input_str = input("Enter a string: ")
    freq = count_characters_frequency(input_str)
    print(f"Character frequencies: {freq}")

# Exercise 10: Reverse a given string
def exercise_10():
    def reverse_string(s):
        return s[::-1]

    input_str = input("Enter a string: ")
    reversed_str = reverse_string(input_str)
    print(f"Reversed string: {reversed_str}")

# Exercise 11: Find the last position of a given substring
def exercise_11():
    def find_last_position(s, sub):
        return s.lower().rfind(sub.lower())

    input_str = input("Enter the main string: ")
    sub_str = input("Enter the substring to find its last position: ")
    last_position = find_last_position(input_str, sub_str)
    print(f"The last position of the substring '{sub_str}' is: {last_position}")

def main():
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

main()