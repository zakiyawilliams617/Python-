Name: Zakiya Williams

Module Info: Module  Assignment 12 : Playoff Elimination Problem Due on 04/18/2026

Approach:
For each team we're testinfg, I build a graph where the source node pushes games through game nodes (one per pair of opposing teams) into teams, and finally into a sinke. The capacity on each edge controls how maany wins can flow where. NetworkX's build in maximum_flow() function then figures out the optimal distribution of game outcomes for us.

The most important thing is how the edge weights from each team node are set to sink. I can them at wins[x] + remaining[x] - wins[i], this represents the maximum number of wins team i is allowed before they surpass team x. If the max flow fills every edge out of the source, there exists at least one scenario where no team beats x so x survives. If the flow falls short, its not possible for x to finish first no matter how the remaining games play out, meaning they are eliminated. 

Known bugs: n/a
Citations: n/a 
