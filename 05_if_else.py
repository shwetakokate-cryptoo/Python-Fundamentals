# Python If-Else Statements - Basic Examples

# If-Else is used for decision making in programming


# Example 1: Simple if statement

age = 18

if age >= 18:
    print("You are an adult")



# Example 2: if-else statement

number = 7

if number % 2 == 0:
    print("\nEven Number")
else:
    print("\nOdd Number")



# Example 3: if-elif-else ladder

marks = 85

print("\nGrade Calculation:")

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")



# Example 4: Nested if statement

age = 20
has_id = True

print("\nEntry Check:")

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Entry Not Allowed")



# Example 5: Using logical operators

username = "admin"
password = "1234"

print("\nLogin Check:")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# Example 6: Short-hand if (one-line)

num = 10

print("\nShort-hand If:")
if num > 5: print("Number is greater than 5")


# Example 7: Ternary Operator (if-else in one line)

age = 16

result = "Adult" if age >= 18 else "Minor"
print("\nTernary Result:", result)



# Example 8: Real-Life Example


print("\n--- ATM Withdrawal System ---")

balance = 5000
withdraw_amount = int(input("Enter amount to withdraw: "))

if withdraw_amount <= balance:
    print("Transaction Successful")
    balance -= withdraw_amount
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")
