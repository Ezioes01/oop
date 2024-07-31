 # Example 1: Creating and manipulating lists
 # Creating a list of numbers 4 numbers = [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
 # Adding elements to the end of the list
numbers.append(6)

# Modifying an element at a specific index

numbers [2] = 10

 # Removing an element by value

numbers.remove(4)

print("Updated list:", numbers) # Output: [1, 2, 10, 5, 6]



# Example 2: List comprehension to create a new list

# Creating a list of squares of numbers from 1 to 5 
squares = [x ** 2 for x in range(1, 6)]

print("Squares:", squares) # Output: [1, 4, 9, 16, 25]



# Example 3: Sorting and reversing a list

numbers = [5, 2, 8, 1, 3]

# Sorting the list
numbers.sort()
print("Sorted list:", numbers) # Output: [1, 2, 3, 5, 8]

# Reversing the list
numbers.reverse()
print("Reversed list:", numbers) # Output: [8, 5, 3, 2, 1]


 # Example 4: Nested lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the matrix print(matrix [1] [2]) # Output: 6


# Example 6: Using lists as stacks and queues

# Stack operations (Last In, First Out LIFO)

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_item = stack.pop()
print("Popped item from stack:", popped_item) # Output: Popped item from stack: 3

# Queue operations (First In, First Out FIFO)
from collections import deque
queue = deque ([1, 2, 3])
queue.append(4)
dequeued_item = queue.popleft()
print("Dequeued item from queue:", dequeued_item) # Output: Dequeued item from queue: 1

# Given a list of numbers, remove all occurrences of a specific number and calculate the sum of remaining numbers.

numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]
remove_num = 3

while remove_num in numbers:
    numbers.remove(remove_num)

print("Numbers after removal:", numbers)
print("Sum of remaining numbers:", sum(numbers))