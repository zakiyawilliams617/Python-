# Prompts user to enter the credit card number (identifier)
# It is stored as a string so we can easily loop through each digit
for i in range(1):
    identifier_number = (input('Please enter identifier: '))

    # Initialize the running total used for the Luhn checksum calculation
    total = 0

    # Stores the length of the identifier number, this helps control the loop ranges when iterating through digits
    length = len(identifier_number)

    # Loop through every other digit starting from the last digit
    # range(start, stop, step)
    # start: length - 1 (last index)
    # stop: -1 (go until the beginning)
    # step: -2 (move left by two positions each time)
    for i in range(length - 1, -1, -2):
        # Convert the data type to an integer
        digit = int(identifier_number[i])
        # Multiply by 2 (Luhn's algorithm)
        digit *= 2

        # if multiply by 2 equals a 1 digit number, add it to the total
        if digit < 10:
            total += digit
        else:
            # if result is a 2 digit number, split the digits and add them together
            # example 15 (1 + 5)
            total += (digit // 10) + (digit % 10)

    # Loop through the numbers that were multiplied by 2, moving left by 2 positions
    for i in range(length - 2, -1, -2):
        total += int(identifier_number[i])

    # Compute the check digit using the Luhn's algorithm
    # Modulo operation results in 0
    check_digit = (10- (total % 10)) % 10

    # Computed check digit to the identifier number
    valid_card_number = identifier_number + str(check_digit)

    # display the 16 digit valid credit number and check digit
    print(f'The valid credit card number is: {valid_card_number} and the newly computed check digit is: {check_digit}')

