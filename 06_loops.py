# Python Loops - Basic Examples & Patterns

# Loops are used to repeat a block of code multiple times

# Example 1: for loop (basic)

print("For Loop Example:")
for i in range(1, 6):
    print(i)


# Example 2: while loop (basic)

print("\nWhile Loop Example:")
i = 1
while i <= 5:
    print(i)
    i += 1


# Example 3: Loop with else

print("\nLoop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")


# Example 4: break statement

print("\nBreak Example:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# Example 5: continue statement

print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Example 6: Nested loops

print("\nNested Loop Example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Example 7: Pattern - Square

print("\nPattern 1: Square")
for i in range(4):
    print("* * * *")


# Example 8: Pattern - Right Triangle

print("\nPattern 2: Right Triangle")
for i in range(1, 5):
    print("* " * i)


# Example 9: Pattern - Inverted Triangle

print("\nPattern 3: Inverted Triangle")
for i in range(4, 0, -1):
    print("* " * i)


# Example 10: Pattern - Number Triangle

print("\nPattern 4: Number Triangle")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Example 11: Real-Life Example

print("\n--- Multiplication Table ---")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
