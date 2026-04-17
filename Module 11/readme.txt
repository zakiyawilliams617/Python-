Name: Zakiya Williams

Module Info: Module  Assignment 11: Hill Cipher Due on 04/12/2026

Approach:
The first setep was identifying the two concerns: the math (linear algebra + modular arithmetic), and the class structure (what each method needs to do). The methods were built starting with simple utility methods so that more complex ones could rely on them. 
1. determinant - everything else depends on knowing the determinant
2. invertible - calls determinant and is needed before any encrypt/decrypt
3. mod_inverse - needed by get_decryption_key
4. encode/decode - convert between strings and NumPy vectors
5. encrypt/decrypt - the code cipher operations
6. get_decryption_key - ties mod_inverse and the adjugate formula together

Known bugs: n/a
Citations: n/a
