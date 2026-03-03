# list of input files, iterate over both in one execution
input_files = ['points1.txt', 'points2.txt']

# process each input file one at a time
for filename in input_files:

    # open the file, read the file
    f = open(filename, 'r')

    # read first line, allow maximum iterations
    max_iterations = int(f.readline().strip())

    # read second line, (n) total number of patients (100)
    n = int(f.readline().strip())

    # read third line, (k) number of clusters/centriods (4)
    k = int(f.readline().strip())

    # calculate amount of patient to cluster (n-k)
    number_patients = n - k

    # read the next k lines, this is the initial centroids (initial infected patients)
    # each line is formatted 'x,y' so I split on ',' to get x and y separately
    # centroids stored as floats because it will become a decimal average later
    centroids = []
    for i in range(k):
        line = f.readline().strip().split(',')
        centroids.append([float(line[0]), float(line[1])])

    # read remaining number_patients lines for patient data points
    # these are the patients I want to cluster to a centriod
    # store them as integers because their coordinates do not change
    patients = []
    for i in range(number_patients):
        line = f.readline().strip().split(',')
        patients.append([int(line[0]), int(line[1])])

    # close file, done reading
    f.close()

    # print initial centroids (4 initially infected patients)
    # convert back to integer for display
    initial = []
    for c in centroids:
        initial.append([int(c[0]), int(c[1])])
    print('Initial COVID-19 Patients:', initial)

    # create empty k cluster, one list for each centroid to hold assigned patients
    # nested list, a list of k lists
    clusters = []
    for i in range(k):
        clusters.append([])

    # track the size of each cluster, from previous iteration
    # initialize to -1, this allows the first iteration to always count a change
    previous_sizes = []
    for i in range(k):
        previous_sizes.append(-1)

    # tracks how many iterations were needed to reach stability
    iterations = 0

    # main k-means loop, runs to max_iterations
    for iteration in range(max_iterations):

        # assign each patient to the closest centroid
        for patient in patients:
            min_distance = -1   # track the smallest distance found so far
            closest = 0         # tracks which centroid is the closest

            for i in range(k):
                # calculate Euclidean distance between patients and centriods
                # use ** 0.5 for square root
                dx = patient[0] - centroids[i][0]
                dy = patient[1] - centroids[i][1]
                distance = (dx ** 2 + dy ** 2) ** 0.5

                # if this centroid is closer than the current closest, update
                if min_distance < 0 or distance < min_distance:
                    min_distance = distance
                    closest = i

            # add this patient to the cluster of the nearest centroid
            clusters[closest].append(patient)

        # check if any clusters sizes changed from last iteration
        # track size changes, not which points moved
        sizes_changed = False
        for i in range(k):
            if len(clusters[i]) != previous_sizes[i]:
                sizes_changed = True

        # if sizes changed, stability has not been reached, increment counter
        if sizes_changed:
            iterations += 1

        # recalculate centroids as the mean of xand y for each cluster
        for i in range(k):
            if len(clusters[i]) > 0:
                # sum up x and y values in this clsuter
                sum_x = 0
                sum_y = 0
                for p in clusters[i]:
                    sum_x += p[0]
                    sum_y += p[1]

                # new centroid is the average/mean x and y
                centroids[i][0] = sum_x / len(clusters[i])
                centroids[i][1] = sum_y / len(clusters[i])

            # save current cluster size for comparison in next iteration
            previous_sizes[i] = len(clusters[i])

        # if no cluster size change, stability is reached, stop
        if not sizes_changed:
            break

        # clear clusters for the next iteration
        # patients will be reassigned to potentially new centroids
        if iteration < max_iterations - 1:
            clusters = []
            for i in range(k):
                clusters.append([])

    # output results
    print('\nIterations to achieve stability:', iterations)

    print('\nFinal Centroids:')
    for c in centroids:
        print(c)

    # print each cluster's size and the last of patients in the cluster
    for i in range(k):
        print('\nNumber of patients in Cluster ' + str(i) + ': ' + str(len(clusters[i])))
        print(clusters[i])

    # blank line between file outputs
    print()
