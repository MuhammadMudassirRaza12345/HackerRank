"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker 
indicating their initial position in the queue from 1 to n.ny person can bribe the person directly in front of them 
to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes,
 or, if anyone has bribed more than two people, print Too chaotic. 
Example:
q=[1,2,3,5,4,6,7,8]

if person 5 bribes person  4, the queue will look like this: 1,2,3,5,4,6,7,8
Only 1 bribe is required. Print 1.

q=[4,1,2,3]

Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.

unction Description

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):

int q[n]: the positions of the people after all bribes
Returns

No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
Input Format

The first line contains an integer t , the number of test cases.
Each of the next t pairs of lines are as follows:
- The first line contains an integer t, the number of people in the queue
- The second line has n space-separated integers describing the final state of the queue.

Now let’s try to understand the problem:

The Persons in the queue are in positions of the first person to 
the last person who wants to have a ride. Thus, the bribe only takes place in one direction from 
the back to the front i.e a person can only bribe someone in a position ahead of him. So, the person 
in the first position will not bribe the person in the second position but the opposite will happen.
 Keep this in mind.

So, for example we have 1,2,3,4,5 assume these numbers as the initial positions of persons who need to have a ride. 
From the sample input, after the bribery schemes we have 2,1,5,3,4. 
It means Person 2 bribed Persons 1 and Person 5 bribed Person 4 and Person 3. 
Also, take not the maximum number of bribes is only two per person. 
Since no one person bribed no more than two persons it satisfies the condition of the maximum bribes
 and hence we print the number of bribes that occurred. In this case, 3.

From the second sample after the bribery scheme we have 2,5,1,3,4. It means after Person 2 bribed P
ersons 1, Person 5 bribed Person 4, 3, and 1 respectively. Take note that a person can only bribe the person 
right in front of him and the maximum number of bribes is 2. Here the sequence can be illustrated as

1.After Person 2 bribery we have [2,1,3,4,5]
2.After Person 5 bribery we have [2,5,1,3,4].
From these observations we can see that Person 5 seems to be greedy and has bribed more than two 
persons hence causing chaos.

Further, since the bribery scheme is basically a swapping of elements in a sorted list, 
to know the number of swaps we can reverse engineer the given sample inputs, say to 2,1,5,3,4 to
their initial positions of 1,2,3,4,5 by placing a counter to counter each swap until each element
reaches their initial positions. From here the comparing sorting algorithm which comes in mind 
should be Bubble Sort. However, a solution with bubble sort will give a time complexity of O(n²)
 which is too much time. We should always favor linear timings of O(n) or less. If you don’t know
  about time complexities I suggest you learn about Big O Time Complexities from Abdul Bari on Youtube.




Sample Input

STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]
Sample Output

3
Too chaotic


"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    q = [i-1 for i in q] # set queue to start at 0
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return
        
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

"""
Input  :

 
2
5
2 1 5 3 4
5
2 5 1 3 4

Your Output :
3
Too chaotic

Expected Output:

3
Too chaotic
"""