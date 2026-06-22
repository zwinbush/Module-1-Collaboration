# Name: Zakai WInbush
# File Name: honor-roll-test.py
# Description: This program accepts student names and GPAs,
# then determines whether the student qualifies for the
# Dean's List or the Honor Roll.

while True:
    # Ask for student's last name
    last_name = input("Enter student's last name (ZZZ to quit): ")

    # Quit if last name is ZZZ
    if last_name == "ZZZ":
        print("Program ended.")
        break

    # Ask for student's first name
    first_name = input("Enter student's first name: ")

    # Ask for GPA
    gpa = float(input("Enter student's GPA: "))

    # Check for Dean's List
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")

    # Check for Honor Roll
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")

    else:
        print(first_name, last_name, "does not qualify for either list.")

    print()  # Blank line for readability