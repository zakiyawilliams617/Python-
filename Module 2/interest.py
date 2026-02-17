# Prompts user to enter the principal amount
Principal = int(input('Principal: '))
# Prompts user to enter the interest rate
Rate = float(input('Rate: '))
# Prompts user to enter term of the certificate of deposit
Term = int(input('Term: '))
# Prompts user to enter number of interest payments
Compound = int(input('Compound:'))

# Shows the output of user inputted investment details (principal, rate, term, and compound)
print(f'Principal: {Principal}\nrate: {Rate}\nTerm: {Term}\nCompound: {Compound}')

# Calculate the total amount, using A=P*(1+r/n)^nt
A = Principal * (1 + Rate / Compound )**(Compound * Term)

# Calculate interest accrued
B = A - Principal

# Summary of calculation results based on user prompts
print(f'Investing ${Principal} in a CD with an {Rate} interest rate  for a term of {Term} '
      f'years (s)  will earn {B} in interest for a total payout of {A}')

