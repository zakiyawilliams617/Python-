# Prompts user to enter the credit card numbers
# It is stored as a string so we can easily loop through each digit by index
for i in range(2):
    card_number = (input('Please enter a credit card number: '))

    # Initialize the running total used for the Luhn checksum calculation
    total = 0

    # Store the length of the credit card
    # Determines which digits to double
    length = len(card_number)

    # Loop through each digit in the credit card number from left to right
    for i in range(length):
        # convert the datatpe to an integer
        digit = int(card_number[i])

        # If the length is even
        # AND the current index is even, the digit is multiplied by 2
        if (length % 2 == 0 and i % 2 == 0):
            # Multiply by 2
            digit *= 2
            # if multiplying by 2 results in a 2 digit number
            # split the digits and add them together
            # Example 15 (1 + 5)
            if digit >= 10:
                tens = digit // 10
                ones = digit % 10
                digit = tens + ones
        # Add processed digit to running total
        total += digit

    # Compute checksum
    # A valid credit card number has checksum = 0
    checksum = total % 10

    # Display the checksum value for each credit card number
    print('Checksum:', checksum)

    # if the checksum = 0, the credit card is valid
    if total % 10 == 0:
        print(f'{card_number} is a valid CC number')
    else:
        # Otherwise, the credit number is valid
        print(f'{card_number} is a invalid CC number')
