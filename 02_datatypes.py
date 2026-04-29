# Data types define the type of value a variable holds


# Example 1: Basic Data Types

# Integer (int)
a = 10

# Float (decimal number)
b = 3.14

# String (text)
c = "Hello, Python"

# Boolean (True / False)
d = True

print("Integer:", a)
print("Float:", b)
print("String:", c)
print("Boolean:", d)


# Example 2: Checking Data Types

print("\nData Types:")
print(type(a))
print(type(b))
print(type(c))
print(type(d))



# Example 3: Type Conversion (Casting)

# Convert int to float
x = 5
y = float(x)

# Convert float to int
p = 6.7
q = int(p)

# Convert int to string
num = 100
text = str(num)

print("\nType Conversion:")
print(y, type(y))
print(q, type(q))
print(text, type(text))



# Example 4: Sequence Data Types

# List (mutable - can change)
my_list = [1, 2, 3, 4]

# Tuple (immutable - cannot change)
my_tuple = (10, 20, 30)

# String (sequence of characters)
my_string = "Python"

print("\nSequence Types:")
print("List:", my_list)
print("Tuple:", my_tuple)
print("String:", my_string)



# Example 5: Set Data Type

# Set (unordered, no duplicate values)
my_set = {1, 2, 3, 3, 4}

print("\nSet:")
print(my_set)  # duplicates removed automatically



# Example 6: Dictionary Data Type

# Dictionary (key-value pairs)
student = {
    "name": "Shweta",
    "age": 18,
    "marks": 90
}

print("\nDictionary:")
print(student)
print("Name:", student["name"])



# Example 7: Real-Life Example

# Storing product details
product_name = "Laptop"      # string
price = 55000.75            # float
in_stock = True             # boolean
features = ["16GB RAM", "512GB SSD"]  # list

print("\nProduct Details:")
print("Name:", product_name)
print("Price:", price)
print("Available:", in_stock)
print("Features:", features)
