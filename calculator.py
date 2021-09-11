print("Welcome to the calculator")

the_first_number = input("Enter the first digit: ")
the_operation = input("Enter the operation to be done +, -, /, *: ")
the_second_number = input("Enter the second digit: ")
if the_operation == "+":
    print(int(the_first_number) + int(the_second_number))
if the_operation == "-":
    print(int(the_first_number) - int(the_second_number))
if the_operation == "/":
    print(int(the_first_number) / int(the_second_number))
if the_operation == "*":
    print(int(the_first_number) * int(the_second_number))

print("Thank you.")
