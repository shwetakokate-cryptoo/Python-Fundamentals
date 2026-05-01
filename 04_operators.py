# Python Operators - Basic Examples

# Operators are used to perform operations on variables and values

# Example 1: Arithmetic Operators

a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)


# Example 2: Comparison (Relational) Operators

x = 5
y = 10

print("\nComparison Operators:")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)


# Example 3: Logical Operators

p = True
q = False

print("\nLogical Operators:")
print("AND:", p and q)
print("OR:", p or q)
print("NOT p:", not p)


# Example 4: Assignment Operators

num = 10

print("\nAssignment Operators:")
num += 5   # num = num + 5
print("After += :", num)

num -= 3   # num = num - 3
print("After -= :", num)

num *= 2   # num = num * 2
print("After *= :", num)

num /= 4   # num = num / 4
print("After /= :", num)


# Example 5: Membership Operators

my_list = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print("Is 3 in list?", 3 in my_list)
print("Is 10 not in list?", 10 not in my_list)


# Example 6: Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators:")
print("a is b:", a is b)     # True (same object)
print("a is c:", a is c)     # False (different objects)
print("a == c:", a == c)     # True (same values)


# Example 7: Real-Life Example

# Checking eligibility for voting
age = int(input("\nEnter your age: "))

print("\nEligibility Check:")
print("Age >= 18:", age >= 18)

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
