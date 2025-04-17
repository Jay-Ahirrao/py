
def exercise_1():
    num = float(input("Enter a number: "))
    print(f"You entered: {num}")


def exercise_2():
    name = "Name"
    is_word = "Is"
    james = "James"
    print(f"{name}{is_word}{james}")


def exercise_3():
    decimal_number = int(input("Enter a decimal number: "))
    print(f"Octal of {decimal_number} is: {oct(decimal_number)}")


def exercise_4():
    float_num = float(input("Enter a float number: "))
    print(f"Formatted float with 2 decimal places: {float_num:.2f}")


def exercise_5():
    float_list = []
    print("Enter 5 float numbers:")
    for i in range(5):
        float_list.append(float(input(f"Enter number {i + 1}: ")))
    print("List of float numbers:", float_list)


def exercise_6():
    try:
        with open("input_file.txt", "r") as file:
            lines = file.readlines()
        
        with open("output_file.txt", "w") as new_file:
            for i, line in enumerate(lines, 1):
                if i != 5:  
                    new_file.write(line)
        print("Content copied to output_file.txt, skipping line 5.")
    except FileNotFoundError:
        print("The file 'input_file.txt' was not found.")


def exercise_7():
    string1, string2, string3 = input("Enter three strings separated by space: ").split()
    print(f"First string: {string1}, Second string: {string2}, Third string: {string3}")


def exercise_8():
    name = "Alice"
    age = 30
    print("Formatted string using .format(): My name is {}, and I am {} years old.".format(name, age))


def exercise_9():
    try:
        with open("sample_file.txt", "r") as file:
            content = file.read()
            if content:
                print("The file is not empty.")
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("The file 'sample_file.txt' was not found.")


def exercise_10():
    try:
        with open("sample_file.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 4:
                print(f"Line 4 content: {lines[3]}")
            else:
                print("The file has fewer than 4 lines.")
    except FileNotFoundError:
        print("The file 'sample_file.txt' was not found.")

def main():
    
    exercise_1()  
    exercise_2()  
    exercise_3()  
    exercise_4()  
    exercise_5()  
    exercise_6()  
    exercise_7()  
    exercise_8()  
    exercise_9()  
    exercise_10()  

main()