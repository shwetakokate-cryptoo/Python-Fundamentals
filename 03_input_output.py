
# Python Input and Output - Basic Examples

# Input: Taking data from the user
# Output: Displaying data to the user


# Example 1: Basic Output using print()


print("Hello, World!")
print("Welcome to Python Programming")



# Example 2: Printing Multiple Values

name = "Shweta"
age = 18

print("\nName:", name)
print("Age:", age)



# Example 3: Using Separator and End

print("\nUsing separator:")
print("Python", "Java", "C", sep=" | ")

print("Using end:")
print("Hello", end=" ")
print("World")



# Example 4: Taking User Input

user_name = input("\nEnter your name: ")
print("Hello,", user_name)

# Note: input() always takes data as string



# Example 5: Taking Numeric Input

# Convert input to integer
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("Sum:", sum_result)



# Example 6: Taking Float Input

length = float(input("\nEnter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle:", area)


# Example 7: Formatted Output (f-strings)

student_name = "Rahul"
marks = 85

print(f"\nStudent {student_name} scored {marks} marks")



# Example 8: Real-Life Example

print("\n--- Student Information ---")

name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print("\nStudent Details:")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
