print("=== Simple Calculator ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

choice = input("Enter choice: ")

if choice == "1":
    result = a + b
elif choice == "2":
    result = a - b
elif choice == "3":
    result = a * b
elif choice == "4":
    if b == 0:
        print("Cannot divide by zero.")
        exit()
    result = a / b
else:
    print("Invalid choice.")
    exit()

print("Result:", result)
