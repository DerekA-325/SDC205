print('Derek Avery - derave1577 - Week 1 Performance Assessment')
name = str(input('What is your name? '))
studentId = str(input('Enter your student ID: '))
print(f'Name: {name}')
print(f'Student ID: {studentId}')

num1 = int(input('Enter a whole number: '))
num2 = int(input('Enter another whole number: '))

add = num1 + num2
mult = num1 * num2
sub = num1 - num2

print(f'The sum of {num1} and {num2} is {add}')
print(f'The product of {num1} and {num2} is {mult}')
print(f'The difference of {num1} and {num2} is {sub}')

if (num1 > num2):
    print(f'{num1} is larger than {num2}')
elif (num1 < num2):
    print(f'{num2} is larger than {num1}')
else:
    print(f'{num1} and {num2} are equal!')
