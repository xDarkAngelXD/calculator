# Functions

def again():
    another = str(input("Have another calculation?"))
    if another.lower().strip() == 'yes':
        define()
    else:
        pass


def add(a, b):
    answer = str(input("How do you want your answer?"))
    if answer.lower().strip() == "absolutevalue":
        print("Your answer is ", abs(a + b))
        again()
    else:
        print(a + b)
        again()


def subtract(a, b):
    answer = str(input("How do you want your answer?"))
    if answer.lower().strip() == "absolutevalue":
        print("Your answer is ", abs(a - b))
        again()
    else:
        print(a - b)
        again()


def multiply(a, b):
    answer = str(input("How do you want your answer?"))
    if answer.lower().strip() == "absolutevalue":
        print("Your answer is ", abs(a * b))
        again()
    else:
        print(a * b)
        again()


def division(a, b):
    answer = str(input("How do you want your answer?"))
    if answer.lower().strip() == "absolutevalue":
        print("Your answer is ", abs(a / b))
        again()
    elif answer.lower().strip() == "remainder":
        print("Your answer is ", (a % b))
        again()
    elif answer.lower().strip() == "integer":
        print("Your answer is ", (a // b))
        again()
    else:
        print(a / b)
        again()


def define():
    a = int(input("So, what is the first number?"))
    b = int(input("Ok, what is the second number?"))
    print("The following will be the choices of arithmetic operations you can perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input("Which of the 4 choices of operation would you like to perform on these numbers?"))

    if operation == 1:
        add(a, b)
    elif operation == 2:
        subtract(a, b)
    elif operation == 3:
        multiply(a, b)
    elif operation == 4:
        division(a, b)
    else:
        print("Please enter a valid option")
        print("Please renter your numbers")
        define()


print("Hi, I am an AI Calculator who can calculate extreme numbers. Feel free to enter any number you like!")
print("By the way, I cannot calculate variables, only constants")
print("I would also like to mention that everything must be spelled correctly or I am no use to you")
define()
