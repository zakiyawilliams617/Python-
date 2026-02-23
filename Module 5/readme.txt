Name: Zakiya Williams

Module Info: Module 5 Assignment: K-means Clustering  Due on 02/22/2026 11:59EST 

Approach:
I start by storing both file names in a list and iterating over them so that both files are processed in a single execution. For each file, I read the parameters line by line using readline(), strip(), and split() to parse the values. The first three lines give maximum iterations, total number of patients(n), and number of clusters(k). Next, I read cluster lines as my initial centroids, and stored tham as floats since they will become decimal averages. The remaining n-k patient coordinates are stored as integers since they don't change.

I used nested lists to represent clusters, a list for k lists, a list for centroids, and a list to track previous cluster sizes initializing to -1 so the first iteration always registers as a change.

The main loop runs up to the maximum iterations. Each iteration assigns every patient to the closest centroid using Euclidean distance calcultions with ** 0.5. I then compare current cluster sizes to previous sizes to check for stability. If any size chagned, I incremented the iteraion counter. I then calculated each centroid as the maean x and y of its assigned patients, saved the current sizes, and cleared the clusters for the next iteration. If no sizes changed, stability is reached and I break out of the loop early. I then printed the outputs.

Known Bugs: N/A

Citations: N/A
