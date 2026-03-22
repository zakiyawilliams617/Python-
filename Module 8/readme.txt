Name: Zakiya Williams

Module Info: Module  Assignment: Linear Feedback Shift Registers  Due on 03/22/2026

Approach: 
Part 1: Building the LFSR
I started by figuring out how the tap position was indexed, this was a challenge. The bits were numbered righ to left and the tap is 1 - indexed from the right, os the formula to tfind the tap's position in the string is N - tap. The step() method works by grabbing the leftmost bit and the tap, XORing them together to produce a new bit, then shifting the entire state left by dropping the leftmost character and appending the new bit on the right.

Part 2: Buidling the Image Encrypter
I figured out that the encrypt and decrypt use the same operation because XOR is its own inverse. When you XOR a value with the same numertwice you get back the original. So I ran the exact same code twice with the same seed and tap to decrypt it.

Known Bugs: n/a
Citations: n/a
