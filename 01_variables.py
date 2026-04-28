# ==========================================
# Python Variables - Basic Examples
# ==========================================

# A variable is used to store data in memory

# Example 1: Storing basic values
name = "Shweta"     # string
age = 18            # integer
height = 5.4        # float
is_student = True   # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# ------------------------------------------
# Example 2: Rules for Naming Variables
# ------------------------------------------

# Valid variable names
user_name = "Alex"
marks1 = 85
_total = 100

# Invalid variable names (uncomment to test errors)
# 1name = "Sam"     # cannot start with number
# user-name = "John" # hyphen not allowed
# class = "FY"       # reserved keyword


# ------------------------------------------
# Example 3: Multiple Assignment
# ------------------------------------------

a, b, c = 10, 20, 30
print("\nMultiple Values:", a, b, c)


# Assign same value to multiple variables
x = y = z = 5
print("Same Value:", x, y, z)


# ------------------------------------------
# Example 4: Changing Variable Value
# ------------------------------------------

score = 50
print("\nInitial Score:", score)

score = 75   # value updated
print("Updated Score:", score)


# ------------------------------------------
# Example 5: Type Checking
# ------------------------------------------

num = 10
print("\nType of num:", type(num))

text = "Hello"
print("Type of text:", type(text))


# ------------------------------------------
# Example 6: Type Casting
# ------------------------------------------

a = "100"
b = int(a)   # convert string to integer

print("\nAfter Type Casting:", b, type(b))


# ------------------------------------------
# Example 7: Simple Real-Life Example
# ------------------------------------------

# Storing student details
student_name = "Rahul"
student_age = 20
student_marks = 88.5

print("\nStudent Details:")
print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
