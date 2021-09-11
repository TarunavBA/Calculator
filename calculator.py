print("Welcome to the calculator")

the_first_number = input(int("Enter the first digit: "))
the_operation = input("Enter the operation to be done +, -, /, *: ")
the_second_number = input(int("Enter the second digit: "))
if the_operation == "+":
    print(the_first_number + the_second_number)
if the_operation == "-":
    print(the_first_number - the_second_number)
if the_operation == "/":
    print(the_first_number / the_second_number)
if the_operation == "*":
    print(the_first_number * the_second_number)

print("Thank you.")
