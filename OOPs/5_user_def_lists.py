# Define the lists
myList = [10, 40, 50, 20, 30, 10, 40, 10]
yourList = ['saw', 'small', 'foxes', 'he', 'six']

# Exercise 1: Append integer 60 into myList
def exercise_1():
    myList.append(60)
    print(f"myList after appending 60: {myList}")

# Exercise 2: Insert 70 on 2nd Position
def exercise_2():
    myList.insert(1, 70)
    print(f"myList after inserting 70 at 2nd position: {myList}")

# Exercise 3: Sort myList in ascending and descending order
def exercise_3():
    myList.sort()
    print(f"myList in ascending order: {myList}")
    myList.sort(reverse=True)
    print(f"myList in descending order: {myList}")

# Exercise 4: Sort yourList in ascending and descending according to length of strings
def exercise_4():
    yourList.sort(key=len)
    print(f"yourList sorted by length (ascending): {yourList}")
    yourList.sort(key=len, reverse=True)
    print(f"yourList sorted by length (descending): {yourList}")

# Exercise 5: Add float value 3.5 into yourList
def exercise_5():
    yourList.append(3.5)
    print(f"yourList after adding 3.5: {yourList}")

# Exercise 6: Use POP and remove method to remove 3.5
def exercise_6():
    yourList.remove(3.5)  # Remove the first occurrence of 3.5
    print(f"yourList after removing 3.5 using remove: {yourList}")
    
    # Alternatively, use POP if we knew the index
    # yourList.pop(yourList.index(3.5))  # Can use this to pop if index is known
    # print(f"yourList after removing 3.5 using pop: {yourList}")

# Exercise 7: Create ourList by merging myList and yourList
def exercise_7():
    ourList = myList + yourList
    print(f"ourList after merging myList and yourList: {ourList}")

# Exercise 8: Find sum of elements in myList
def exercise_8():
    total_sum = sum(myList)
    print(f"Sum of elements in myList: {total_sum}")

# Exercise 9: Find smallest, largest and second largest number in myList
def exercise_9():
    smallest = min(myList)
    largest = max(myList)
    sorted_list = sorted(myList)
    second_largest = sorted_list[-2] if len(sorted_list) > 1 else None
    print(f"Smallest number in myList: {smallest}")
    print(f"Largest number in myList: {largest}")
    print(f"Second largest number in myList: {second_largest}")

# Exercise 10: Count occurrences of all elements in a list
def exercise_10():
    element_count = {elem: myList.count(elem) for elem in set(myList)}
    print(f"Occurrences of all elements in myList: {element_count}")

# Exercise 11: Perform Data slicing to display string elements from ascending sorted yourList
def exercise_11():
    # Sorting yourList in ascending order first
    yourList.sort()
    
    # a. Display ‘saw’, ‘six’, ‘small’
    print(f"a. Display: {yourList[:3]}")
    
    # b. Use negative indices to display: ‘six’, ‘small’, ‘foxes’
    print(f"b. Display using negative indices: {yourList[-3:]}")

    # c. All elements after mid of the list (In both directions)
    mid = len(yourList) // 2
    print(f"c. All elements after mid: {yourList[mid:]}")
    
    # d. Alternate elements in both directions from the middle of the list
    print(f"d. Alternate elements from middle: {yourList[mid::2]}")

# Main function to execute all exercises
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

# Call the main function
if _name_ == "_main_":
    main()