def functionOne():
    print("My student ID is derave1577.")

def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a second number: "))
    answer = num1 + num2
    print(f'The sum of {num1} and {num2} is {answer}.')
    return answer

def functionThree(num1):
    Id = 1577
    if (num1 > 5):
        print("The sum is greater than 5.")
    else:
        print("The sum is less than or equal to 5.")
    return Id

def main():
    # Function one prints my student Id.
    functionOne()

    # Function two takes two user inputs and adds them together.
    num1 = functionTwo()

    # Function three takes the returned sum from function two and checks if it is greater than 5, then returns the numeric part of my student id.

    idNum = functionThree(num1)

    print(f'The returned value of functionThree is {idNum}')

main()
