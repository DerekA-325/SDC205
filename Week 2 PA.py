print("derave1577")

name = str(input("Enter your name: "))
studentId = str(input("Enter your student id: "))

print(f'Hello {name}! Student Id: {studentId}')

answer = 4
guessCount = 0
guess = 0

while guess != answer:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > 10 and guess < 1:
        print("Invalid guess")
    elif guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        print("You got it!")
    guessCount = guessCount + 1
print(f'You took {guessCount} guesses!')

print("Output from the while loop: ")
count = 0
increment = 0
while count < 5:
    increment = increment + 1
    count = count + 1
    print(f'{guess} incremented by {increment} is {guess + increment}')

print("Output from the for loop: ")
increment = 0
for i in range(5):
    increment = increment + 1
    print(f'{guess} incremented by {increment} is {guess + increment}')

