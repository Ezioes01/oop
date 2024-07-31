set1 = { 1, 2, 3, 4 }
set2 = { 3, 4, 5, 6 }

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_difference_set = set1 ^ set2

even_numbers = {x for x in range( 1,11 ) if x % 2 == 0}

# Example 1: Working with dictionaries

# Creating a dictionary of students grades
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}

# Accessing the value using keys
print( "bob's grade is ", grades[ "Bob"] ) #Output: bob's grade is 92

# Adding a new entry
grades[ "Eve" ] = 90

# Interating through the dictionary
for student, grade in grades.items():
  print(f"{student}: {grade}")

# Using get() method to avoid KeyError
print("Frank's grade:", grades.get( 'Frank','Grade not found' ))

# Example 2: Set operations

