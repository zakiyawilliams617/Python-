Name: Zakiya Williams

Module Info: Module  Assignment 13: The Dining Philosopher's Problem  Due on 04/26/2026

Approach:
For this assigment the challenge is making sure none of the philosophers get stuck waiting forever for a fork, deadlock. Each philosopher will only eat if both forks are available at the same time. If a philosopher picks up their left fork but their right form is already taken, they put the left fork back down and try again later instead of just sitting there holding on fork and waiting. 

To make all 5 philosophers run at the same time independently, each one is set up as its own thread, meaning they all operate simultaneously just like real people sitting at a table would. The main program starts all 5 threadsm lets tem run for 10 secondsm then signals everyone to stop and waits for them all to finish before closing out.

Known bugs: n/a
Citations: n/a
