Name: Zakiya Williams

Module Info: Module 6 Assignment: Space Domain Awareness & Approximating Pi  Due on 03/01/2026 11:59EST 

Approach: For sda.py, the overall approach was to break the problem into small functions rather than wirting everything in one block. Read_telemetry handles only file reading and parsing, check_collisions handles only the logic, keeping them separate makes each piece easier to test and debug. For the collision checking I used iteratools to avoid writing nested loops. This makes sure every unique pair of satellites gets checked exactly once without comparing a satellite to itself or checking the same pair twice. When a collision is found, both countries get added to the other's list. The output is handled in the mail block, which loops  through both files and builds the output at the same time for the console and the file.

For bbp.py, I was thinking about recursion. Instead of building from k=0, the function started at k=10 and works its way down, with k=0 as the base case. Each call computes its own term and adds it to the result of the next recursive call down. This means the print counts down from 10 to 0, so it matches the output. The base case returns k=0 without making another recursive call, which is what stops the recursion from going on forever. I wanted to keep things simple and readable.

Known Bugs: n/a 
Citations: n/a
