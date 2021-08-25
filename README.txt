Hetansh Patel 
CS 370 - HW4 

A. This package includes the following files. 

|-- scheduler.py        [ The core of all the files , this file implements 3 scheduling algorithms and inputs processes.csv file while has the input values ]
|-- processes.csv       [ it has all the input values]
|-- README.txt          [ This file contains questions answered from the Homework PDF s]  

B. Running the scheduler file 

command line argument  - python3 scheduler.py processes.csv 4(any value for time quantum)

C. Question 
1. What is the other name for Shortest Job First Preemptive Algorithm?
    A) It is also called Shortest Job next or Shortest process next 
2. What are the 5 different states a process can be in scheduling (Look into process state
diagram)?
    A) Five different states : 
        1) new
        2) ready 
        3) running
        4) waiting 
        5) terminated 
3. Shortest Job First is like Priority Scheduling with the priority based on ______ of the process?
    A) First Come First Serve Process 
4. ________ effect is the primary disadvantage of First Come First Serve Scheduling algorithm.
    A) Convoy Effect 
5. How does Multi Level Feedback queue prevent starvation of processes that waits too long in
lower priority queue?
    A) It moves a process which is waiting for a longer time from lower priority queue to Higher Priority Queue. 