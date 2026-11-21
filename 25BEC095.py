"""Assignment 1: Basics of Python Programming.

Run with: python Assignment_1.py
Choose an exercise from the menu. No third-party packages are required.
"""

from pathlib import Path


def read_number(prompt):
    """Read a valid integer or decimal number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_integer(prompt):
    """Read a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def basic_operations():
    print("\n1. Basic Python Operations")
    first = read_number("Enter the first number: ")
    second = read_number("Enter the second number: ")
    print(f"Sum: {first + second:g}")
    print(f"Difference: {first - second:g}")
    print(f"Product: {first * second:g}")
    if second == 0:
        print("Quotient and remainder are undefined when the second number is zero.")
    else:
        print(f"Quotient: {first / second:g}")
        print(f"Remainder: {first % second:g}")


def lists_and_tuples():
    print("\n2. Lists and Tuples")
    numbers = []
    for index in range(10):
        numbers.append(read_integer(f"Enter number {index + 1} of 10: "))
    print("Starting list:", numbers)

    numbers.append(read_integer("Enter a number to add: "))
    print("After adding:", numbers)

    remove_value = read_integer("Enter a value to remove: ")
    if remove_value in numbers:
        numbers.remove(remove_value)
        print("After removing the first matching value:", numbers)
    else:
        print("That value is not in the list; the list is unchanged.")

    insert_value = read_integer("Enter a value to insert: ")
    position = read_integer(f"Enter its position (0 to {len(numbers)}): ")
    if 0 <= position <= len(numbers):
        numbers.insert(position, insert_value)
    else:
        print("Position out of range; the value was not inserted.")

    print("Final list:", numbers)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Tuple:", tuple(numbers))


def strings():
    print("\n3. Strings")
    value = input("Enter a string: ")
    letters = [char.casefold() for char in value if char.isalpha()]
    vowels = sum(char in "aeiou" for char in letters)
    consonants = len(letters) - vowels
    normalized = "".join(char for char in value.casefold() if char.isalnum())
    print("Number of characters:", len(value))
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Reversed string:", value[::-1])
    print("Palindrome (ignoring spaces, punctuation, and case):", normalized == normalized[::-1])


def sets_and_dictionaries():
    print("\n4. Sets and Dictionaries")
    set_a = {int(item.strip()) for item in input("Enter integers for set A, separated by commas: ").split(",") if item.strip()}
    set_b = {int(item.strip()) for item in input("Enter integers for set B, separated by commas: ").split(",") if item.strip()}
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Union:", set_a | set_b)
    print("Intersection:", set_a & set_b)
    print("Difference (A - B):", set_a - set_b)
    print("Symmetric difference:", set_a ^ set_b)

    students = {}
    print("Enter the names and marks of five students:")
    for index in range(5):
        name = input(f"Student {index + 1} name: ").strip()
        marks = read_number(f"{name}'s marks: ")
        students[name] = marks
    print("Student marks:", students)
    highest_name = max(students, key=students.get)
    print(f"Highest marks: {highest_name} ({students[highest_name]:g})")


def gpa_calculator():
    print("\n5. GPA Calculator")
    count = read_integer("How many courses? ")
    while count <= 0:
        print("Enter at least one course.")
        count = read_integer("How many courses? ")

    weighted_points = 0.0
    total_credits = 0.0
    for index in range(count):
        print(f"Course {index + 1}")
        grade_point = read_number("  Grade point: ")
        credit = read_number("  Credits: ")
        while credit <= 0:
            print("  Credits must be greater than zero.")
            credit = read_number("  Credits: ")
        weighted_points += grade_point * credit
        total_credits += credit
    print(f"GPA: {weighted_points / total_credits:.2f}")


def factorial(number):
    """Return n! for a non-negative integer n."""
    if number < 0:
        raise ValueError("Factorial is not defined here for negative integers.")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def fibonacci(terms):
    """Return the requested number of Fibonacci terms."""
    if terms < 0:
        raise ValueError("The number of terms cannot be negative.")
    sequence = []
    first, second = 0, 1
    for _ in range(terms):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def is_prime(number):
    """Return whether number is prime."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def functions_and_iteration():
    print("\n6. Functions and Iteration")
    number = read_integer("Enter a non-negative integer for factorial: ")
    try:
        print(f"{number}! = {factorial(number)}")
    except ValueError as error:
        print(error)
    terms = read_integer("How many Fibonacci terms? ")
    try:
        print("Fibonacci series:", fibonacci(terms))
    except ValueError as error:
        print(error)
    candidate = read_integer("Enter an integer to check for primality: ")
    print(f"{candidate} is {'prime' if is_prime(candidate) else 'not prime'}.")


def file_handling():
    print("\n7. File Handling")
    name = input("Enter student name: ").strip()
    roll_number = input("Enter student roll number: ").strip()
    department = input("Enter department: ").strip()
    details = f"Name: {name}\nRoll number: {roll_number}\nDepartment: {department}\n"
    output_path = Path(__file__).with_name("student_details.txt")
    output_path.write_text(details, encoding="utf-8")
    print(f"Student details written to {output_path.name}. File contents:")
    print(output_path.read_text(encoding="utf-8"))


def exception_handling():
    print("\n8. Exception Handling")
    numerator = read_number("Enter the numerator: ")
    denominator = read_number("Enter the denominator: ")
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
    else:
        print(f"Result: {result:g}")


def list_comprehension():
    print("\n9. List Comprehension")
    squares = [number**2 for number in range(1, 21)]
    evens = [number for number in range(1, 51) if number % 2 == 0]
    divisible_by_three_and_five = [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]
    print("Squares of 1 to 20:", squares)
    print("Even numbers from 1 to 50:", evens)
    print("Numbers divisible by both 3 and 5 from 1 to 100:", divisible_by_three_and_five)


def student_record_menu():
    print("\n10. Student Record Manager")
    students = {}
    while True:
        print("\n1. Add a student\n2. Update marks\n3. Search for a student\n4. Delete a student\n5. Display all records\n0. Return to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Student name: ").strip()
            if not name:
                print("Name cannot be empty.")
            elif name in students:
                print("That student already exists. Choose update marks to change their marks.")
            else:
                students[name] = read_number("Marks: ")
                print("Student added.")
        elif choice == "2":
            name = input("Student name to update: ").strip()
            if name in students:
                students[name] = read_number("New marks: ")
                print("Marks updated.")
            else:
                print("Student not found.")
        elif choice == "3":
            name = input("Student name to search: ").strip()
            if name in students:
                print(f"{name}: {students[name]:g} marks")
            else:
                print("Student not found.")
        elif choice == "4":
            name = input("Student name to delete: ").strip()
            if students.pop(name, None) is not None:
                print("Student deleted.")
            else:
                print("Student not found.")
        elif choice == "5":
            if students:
                for name, marks in students.items():
                    print(f"{name}: {marks:g} marks")
            else:
                print("No student records yet.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please choose 0 to 5.")


EXERCISES = {
    "1": basic_operations,
    "2": lists_and_tuples,
    "3": strings,
    "4": sets_and_dictionaries,
    "5": gpa_calculator,
    "6": functions_and_iteration,
    "7": file_handling,
    "8": exception_handling,
    "9": list_comprehension,
    "10": student_record_menu,
}


def main():
    while True:
        print("\nAssignment 1: Basics of Python Programming")
        for number, title in [
            (1, "Basic Python Operations"),
            (2, "Lists and Tuples"),
            (3, "Strings"),
            (4, "Sets and Dictionaries"),
            (5, "GPA Calculator"),
            (6, "Functions and Iteration"),
            (7, "File Handling"),
            (8, "Exception Handling"),
            (9, "List Comprehension"),
            (10, "Mini Programming Problem"),
        ]:
            print(f"{number}. {title}")
        print("0. Exit")
        choice = input("Choose an exercise (0-10): ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        exercise = EXERCISES.get(choice)
        if exercise is None:
            print("Invalid choice. Please choose a number from 0 to 10.")
        else:
            exercise()


if __name__ == "__main__":
    main()

