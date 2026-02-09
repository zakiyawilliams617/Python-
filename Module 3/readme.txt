Name: Zakiya Williams

Module Info: Module 3 Assignment: Credit Card Checksum  Due on 02/08/2026 11:59EST 

Approach:

luhn_verify.py
The approach I took to verify the credit card numbers, using Luhn’s algorithm was by iterating through the digits and computing a checksum based on the position specific rules. I stored the credit card number as a string so that I could access individual digits by index, then converted each digit to an integer during processing. Working right to left, I doubled every other digit beginning with the last digit, and if the doubled value resulted in a two digit number, I split the digits using integer division and modulo and added them together before adding the result to a running total. One challenge I encountered early on was with the checksum validation logic (if total % 10 == 0) inside the digit processing loop, which caused the program to print the result multiple times (5 to be exact). Through debugging, I realized that the checksum should only be evaluated after all digits have been processed, which reinforced my understanding of spacing with loop scope and execution flow. This process helped me clearly separate calculation logic from output logic and ensured the program printed a single, correct validation result per credit card number.

luhn_generate.py                                                                                                   To generate a valid 16 digit credit card number, using Luhn’s algorithm and compute the check digit started with me storing the intial 15 digit number. I then applied the right to left Luhn process to this identifer number, doubling every other digit starting from the far right position and summing all processed digits into a running total. Initially, I struggled with incorrect syntax such as writing check_sum = (10 - (total - %10)), which helped me better understand how modulo operations work in Python and how assignment differs from expressions. After correcting this, I computed the check digit using the formula (10 - (total % 10)) % 10, which ensures the final total becomes divisible by 10. Finally, I computed check digit using the idenitifer number to get a valid 16 digit credit card number. This task helped me better understand of the difference between checksum calculation and check digit generation, as well as how small syntax errors can reveal important conceptual gaps when working through algorithms.
                                                                                                                  
Known Bugs:
N/A

Citation:
N/A
