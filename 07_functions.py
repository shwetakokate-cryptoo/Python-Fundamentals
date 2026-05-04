# Python Functions - Modular Coding Examples

# A function is a block of code that performs a specific task
# It helps in code reusability and better organization

# Example 1: Simple Function

def greet():
    print("Hello, Welcome to Python!")

greet()


# Example 2: Function with Parameters

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Shweta")


# Example 3: Function with Return Value

def add(a, b):
    return a + b

result = add(10, 5)
print("\nSum:", result)


# Example 4: Default Parameters

def greet_with_default(name="Guest"):
    print(f"Hello, {name}")

greet_with_default()
greet_with_default("Rahul")


# Example 5: Keyword Arguments

def student_details(name, age):
    print(f"\nName: {name}, Age: {age}")

student_details(age=18, name="Shweta")


# Example 6: Arbitrary Arguments (*args)

def total_marks(*marks):
    total = sum(marks)
    print("\nTotal Marks:", total)

total_marks(80, 85, 90)


# Example 7: Returning Multiple Values

def calculate(a, b):
    return a + b, a * b

sum_result, product_result = calculate(4, 5)

print("\nSum:", sum_result)
print("Product:", product_result)


# Example 8: Lambda Function (Anonymous Function)

square = lambda x: x * x

print("\nSquare of 5:", square(5))


# Example 9: Real-Life Example (Modular Code)

# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to display result
def display_result(number):
    result = check_even_odd(number)
    print(f"\nNumber {number} is {result}")

# Main program
num = int(input("\nEnter a number: "))
display_result(num)
