try:
    # Take user inputs
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))

    # Check if age is negative
    if age < 0:
        print("Age cannot be negative")
    else:
        # String concatenation for full name
        full_name = first_name + " " + last_name
        print("Full Name:", full_name)

        # Age next year
        print("You will be", age + 1, "next year")

except ValueError:
    print("Invalid age input")