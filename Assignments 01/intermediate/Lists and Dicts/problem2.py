# PROJECT 4 ASSIGNMENTS 

# AUTHOR : Aqsa Bhatti

# ASSIGNMENTS 01

# 02_intermediate

# Lists and Dicts

# problem2.py

# PROBLEM # 2 : INDEX GAME

# PROBLEM STATEMENT
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.

# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.

# SOLUTION:

def access_element(my_list, index):
    """✨ Function to access an element from the list ✨"""
    if 0 <= index < len(my_list):
        return f"\n 📋 Element at index {index}: {my_list[index]}"
    else:
        return "\n ⚠️ Invalid index! Out of range."

def modify_element(my_list, index, new_value):
    """✨ Function to modify an element in the list ✨"""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"\n ✅ Updated list: {my_list}"
    else:
        return "\n ⚠️ Invalid index! Out of range."

def slice_list(my_list, start, end):
    """✨ Function to return a sliced part of the list ✨"""
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list) and start < end:
        return f"\n 🔪 Sliced list: {my_list[start:end]}"
    else:
        return "\n ⚠️ Invalid indices for slicing!"

def main():
    print(f"\n 👋 Welcome to the Interactive List Manager! 🌟")
    print(f"\n 📋 Manage your list by accessing, modifying, or slicing it. Let's get started! 🚀\n")

    my_list = [10, 'apple', 25.5, 'banana', 100]

    while True:
        print(f"\n✨ Options:")
        print("\n 1️⃣  Access an element")
        print("\n 2️⃣  Modify an element")
        print("\n 3️⃣  Slice the list")
        print("\n 4️⃣  Exit")
 
        choice = input(f"\n 💬 Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            index = int(input("\n 🔍 Enter the index: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input(f"\n 🔧 Enter the index: "))
            new_value = input(f"\n ✍️ Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input(f"\n 🔢  Enter the start index: "))
            end = int(input(f"\n 🔢  Enter the end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print(f"\n👋 Exiting the program. Goodbye! 🌈")
            break
        else:
            print(f"\n ❌ Invalid choice! Please select a valid option. 🔁")

if __name__ == "__main__":
    main()

# ------------------------------ END OF CODE --------------------------------