"""
You are given an unordered array consisting of consecutive integers E [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

Example
arr = [7, 1, 3, 2, 4, 5, 6]

perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took 5 swaps to sort the array.

Function Description

Complete the function minimumSwaps in the editor below.

minimumSwaps has the following parameter(s):

int arr[n]: an unordered array of integers
Returns

int: the minimum number of swaps to sort the array

Input Format
The first line contains an integer, n, the size of arr.
The second line contains n space-separated integers arr[i].

Sample Input 0

4
4 3 1 2
Sample Output 0

3
Explanation 0

Given array arr: [4,3,1,2]
After swapping (0,2) we get arr: [1,3,4,2]
After swapping (1,2) we get arr: [1,4,3,2]
After swapping (1,3) we get arr: [1,2,3,4]
so, we need a minimum of 3 swaps to sort the array in ascending order.


"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    tmp = {}

    for i, val in enumerate(arr):
        tmp[val] = i

    for i in range(len(arr)):
        # because they are consecutives, I can see if the number is where it belongs
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[tmp[i+1]] = t

            # Switch also the tmp array, no need to change i+1 as it's already good now
            tmp[t] = tmp[i+1]

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
