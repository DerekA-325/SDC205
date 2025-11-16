print("derave1577")
# This program calculates the ending principle in a bank
# account after compounding interest.

p = float(input('Enter the starting principle: '))
r = float(input('Enter the annual interest rate: '))
n = int(input('How many times per year is the interest compounded? '))
t = int(input('For how many years will the account earn interest? '))

# Adjust the interest rate.

r = r/100

# Calculate the ending balance

a = p * (1 + float(r) / n) ** (n * t)

# Display the ending balance

print(f'At the end of {t} yers you will have ${a:,.2f}')
