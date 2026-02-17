import math # Gives access to python's math library
t = 157788000 # total time of the simulation in seconds
dt = 25000 # time step in seconds (delta time)
start_time = 0 # start time at zero

# Input data for each planet using a Python list:
#          [x position, y position, x velocity, y velocity, and mass]

earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

# List of planets containing the input data for the calculations
planets = [earth, mars, mercury, venus]
planet_names = ['earth', 'mars', 'mercury', 'venus']

while start_time < t: # Outer while loop, runs until total simulation time is reached
    for i in range(len(planets)): # Inner for loop, loops through each planet in the list
        planet = planets[i]

        # 1. Calculating the Total Force
        G = 6.67e-11 # defining the gravitational constant
        dx = sun[0] - planet[0] # delta x, sun [0] input of x position, planet[0] input of x position
        dy = sun[1] - planet[1] # delta y, sun [1] input of y position, planet[1] input of y position
        r = (dx**2 + dy**2)**0.5  # radius,the distance between the sun and the planet,
                    # using **0.5 as an exponent in place of square root

        total_force = G * sun[4] * planet[4] /r**2 #  formula for total force F = G * (m1*m2)/ r^2

        # 2. Calculating the x and y components of the force
        Fx = total_force * dx / r  # force of x component/x-axis
        Fy = total_force * dy / r  # force of y component/y-axis

        # 3. Calculating the x and y components of the acceleration
        ax= Fx / planet[4]  # acceleration of x, planet[4] inputs the mass of planet in loop
        ay= Fy / planet[4]  # acceleration of y

        # 4. Calculating the x and y components of the velocity
        vx = planet[2] + (ax * dt) # new velocity of x, using v not * planet[2] input of the x velocity of planet in loop
        vy = planet[3] + (ay * dt) # new velocity of y, using v not * planet[3] inout of the y velocity of planet in loop

        # 5. Calculating the x and y components of the new position
        px = planet[0] + vx * dt # new position of x, planet[0] input of old position of x
        py = planet[1] + vy * dt # new position of y, planet[1] input of old position of y

        # Update the planet data with new values
        planet[0] = px # new x position
        planet[1] = py # new y position
        planet[2] = vx # new x velocity
        planet[3] = vy # new y velocity

    # Updated time
    start_time = start_time + dt

# Output for each planet using the same list format from the beginning
    # [x position, y position, x velocity, y velocity, and mass]
print(f'{earth[0]: .4e} {earth[1]: .4e} {earth[2]: .4e} {earth[3]:.4e} {earth[4]:.4e}')
print(f'{mars[0]: .4e} {mars[1]: .4e} {mars[2]: .4e} {mars[3]:.4e} {mars[4]:.4e}')
print(f'{mercury[0]: .4e} {mercury[1]: .4e} {mercury[2]: .4e} {mercury[3]:.4e} {mercury[4]:.4e}')
print(f'{sun[0]: .4e} {sun[1]: .4e} {sun[2]: .4e} {sun[3]:.4e} {sun[4]:.4e}')
print(f'{venus[0]: .4e} {venus[1]: .4e} {venus[2]: .4e} {venus[3]:.4e} {venus[4]:.4e}')