try:
    grade = int(input("Enter your grade level: "))

    if grade in [7, 8, 9, 10, 11, 12]:
        print("Valid grade level.")
    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid input. Please enter a whole number.")