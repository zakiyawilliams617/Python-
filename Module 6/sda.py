# import itertools library to use for satellite pair checking
import itertools

# define the function that accepts the input file name as a string
def read_telemetry(file_name): 

    file = open(file_name, 'r') # open the file in read mode
    n = int(file.readline().strip())  # read the first line and convert to integer (satellite count)
    satellites = [] # create an empty list to store satellite data
    
    # loop n times, once for each satellite
    for i in range(n):

        # read the next line and remove newline
        # split the line by comma into (country, altitude, velocity)
        # first element is the country name
        # second element is altitude, convert to an integer 
        # third element is velocity, convert to a float
        # add this satellite as a list to satellites

        line = file.readline().strip() 
        parts = line.split(',') 
        country = parts[0] 
        altitude = int(parts[1]) 
        velocity = float(parts[2]) 
        satellites.append([country, altitude, velocity]) 

    # close the file after reading
    file.close()

    # return the list of satellite data
    return satellites 

# define function that accepts the satellite data list
def check_collisions(satellites):  
    
    # create empty dictionary to map each country to its list of collision risks
    collision_dict = {}  

    # loop through each satellite to initialize the dictionary
    for i in range(len(satellites)):  

        # set each country's collision list to empty
        collision_dict[satellites[i][0]] = []  

    # iterate over every unique pair of satellites
    for sat1, sat2 in itertools.combinations(satellites, 2):  

        country1 = sat1[0]  # unpack country for satellite 1
        altitude1 = sat1[1]  # unpack altitude for satellite 1
        velocity1 = sat1[2]  # unpack velocity for satellite 1
        country2 = sat2[0]  # unpack country for satellite 2
        altitude2 = sat2[1]  # unpack altitude for satellite 2
        velocity2 = sat2[2]  # unpack velocity for satellite 2

        # only check collision if both satellites share the same altitude
        if altitude1 == altitude2:  

            # opposite directions = collision risk
            if (velocity1 > 0 and velocity2 < 0) or (velocity1 < 0 and velocity2 > 0):  

                # add country2 to country1's risk list
                collision_dict[country1].append(country2)  

                # add country1 to country2's risk list
                collision_dict[country2].append(country1)  


            elif (velocity1 > 0 and velocity2 > 0) or (velocity1 < 0 and velocity2 < 0):  # same direction
                # different speeds = collision risk
                if velocity1 != velocity2:  

                    # add country2 to country1's risk list
                    collision_dict[country1].append(country2)  

                    # add country1 to country2's risk list
                    collision_dict[country2].append(country1)  

    # return the dict of collision results
    return collision_dict  

# only run the code below if this file is executed directly
if __name__ == "__main__":  

    # list of the two input file names
    input_files = ["satellites1.txt", "satellites2.txt"]  

    # loop through each input file one at a time
    for i in range(len(input_files)):  

        # call read_telemetry to get satellite data from file
        satellites = read_telemetry(input_files[i])  


        # call check_collisions to get collision results
        collision_dict = check_collisions(satellites)  

        # simulation number is 1-based (1 or 2)
        sim_number = i + 1  
        # build the header string
        header = "##### Space Command Simulation " + str(sim_number) + " #####"  

        if i > 0:  # print a blank line before every simulation except the first
            print()
        print(header)  # print the header to console

        output_lines = [header]  # start the output list with the header for writing to file later

        # loop through each satellite to print/store its collision status
        for sat in satellites:  

            # get the country name from this satellite
            # look up its collision list in the dict

            country = sat[0]  
            collisions = collision_dict[country]  

            # if no collisions, print the safe message
            if len(collisions) == 0:  
                line = country + " is not at risk for a collision."
            else:  # otherwise print which countries it will collide with
                line = country + " is at risk of colliding with " + str(collisions)
            
            # print the line to console
            print(line)  
            output_lines.append(line)  # add the line to our output list

        out_file_name = "satellites" + str(sim_number) + "_alerts.txt"  # build the output file name

        out_file = open(out_file_name, "w")  # open the output file in write mode

        for line in output_lines:  # loop through each line to write to the file

            out_file.write(line + "\n")  # write the line followed by a newline character

        out_file.close()  # close the output file when done