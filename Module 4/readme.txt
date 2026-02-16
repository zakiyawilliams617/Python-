Name: Zakiya Williams

Module Info: Module 4 Assignment: N-body Simulation  Due on 02/15/2026 11:59EST 

Approach:
The approached used is two nested loops, an outer while loop that advances the simulation through times, the inner for loop that processes each planet individually at every time step. This approach was chosen because it allows the program to update all planets before mvoing forward in time, this is ensures every calculation for a given moment uses accurate and consistent position data.

Each planet's data is stored as a Python list containing five objects (x positon, y position, x velocity, y velocity, and mass). This data structure was chosen because lists allow access to every object by indexing, making it easy to read specifics like planet[0] for x position and updating them in place. 

All planets are in a single list of lists, this enables the for loop to iterate through them. Notice, the sun is not included in the list of planets, it remains fixed at the origin throughout the entire simulation, which makes sense given the sun's mass is much larger than the planets. 

Known Bugs:
I encountered two related overflow erros that revealed  problems with the physics calculations. The first error, "Complex exponentiation..." occured because of a missing set of parenthesis in the distance calculation. I wrote r = dx**2 = dy**2**0.5, which Python interpreted as dx^2 + sqrt of dy^2, instead of sqrt of (dx^2 + dy^2). This incorrect calculation can produce negative values when dx^2 was large enough, adn taking the square root of a negative number creates a complex number in Python. The "Complex exponentiation..." error occurred when it was trying to calculate the force using r**2  because it was trying to square a complext number in a instead of a real number.

After fixing the error by adding parenthesis to r = (dx**2 + dy*2)**0.5, I encountered a different overflow error: "... 'Result too large'". This error indicated that the distnace values were growing beyond Python's limits. The cause of this error was an incorrect position. I wrote px = (planet[0] + planet[2]) 8 vx, which multipled the position by the velocity instead of implementing the proper calculation. I corrected this error but updating it to px = planet[0] + vx * dt and py = planet[1] + vy 7 dt.

Lastly,the update time syntax was inside the planet loop, causing time to advance four times per iteration instead of one time, this also contributed. Moving start_time = start_time + dt outside the loop ensured time advanced correctly, allowing the simulation to run to complete. 

Citation:
Python F-string Tutorial. ZetCode. https://zetcode.com/python/fstring/

