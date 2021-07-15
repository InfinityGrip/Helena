#adding function
def add(num1, num2):

    return num1 + num2

#substraction function
def substract(num1, num2):

    return num1 - num2


#multiplication function
def multiply(num1, num2):

    return num1 * num2


#division function
def divide(num1, num2):

    return num1 / num2


print("select operation.\n1.Add\n2.Substraction\n3.Multiplication\n4.Divide")

while True:

    choose = input("enter 1,2,3, or 4 for each operation:\n")

    if (choose in ('1', '2', '3', '4')):

        num1 = float(input("enter first number:\n"))

        num2 = float(input("enter second number:\n"))

        if(choose == '1'):

            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choose == '2':

            print(f"{num1} - {num2} = {substract(num1, num2)}")

        elif choose == '3':

            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choose == '4':

            print(f"{num1} / {num2} = {divide(num1, num2)}")
            break
    else:
        print("The operation you inserted is not available, please try again.")


