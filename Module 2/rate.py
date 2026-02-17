# Prompts user to enter the principal amount
Principal = float(input('Principal: '))
# Prompts user to enter the total amount paid
Total = float(input('Total: '))
# Prompts user to enter term of the certificate of deposit
Term = int(input('Term: '))
# Prompts user to enter number of interest payments per year
Compound = int(input('Compound:'))

# Shows the output of user inputted investment details (principal, rate, term, and compound)
print(f'Principal: {Principal}\nTotal: {Total}\nTerm: {Term}\nCompound: {Compound}')

# Calculate the rate, using r= n [(A/P)^(1/nt)-1]
Rate = Compound * ((Total / Principal) ** (1 / (Compound * Term)) - 1)

# Summary of calculation results based on user prompts
print(f'The interest rate on a ${Principal} CD that pays out ${Total} over a {Term} year term is {Rate:%}')
