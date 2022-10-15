"""
Given a 6x6 2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
a b c
  d
e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass 
sum for every hourglass in arr, then print the maximum hourglass sum.The array will always be 6x6.
Example
arr =
-9 -9 -9  1 1 1
0 -9  0  4 3 2
-9 -9 -9  1 2 3
0  0  8  6 6 0
0  0  0 -2 0 0
0  0  1  2 4 0
The 16 hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
9,  17, 25, 18
The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:
0 4 3
  1
8 6 6

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers
Returns

int: the maximum hourglass sum
Input Format

Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].

Constraints:
-9 <= arr[i][j] <= 9
0 <= i,j <= 5



Output Format
print the largest (maximum) hourglass sum found in arr.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19

"""
# n = 6
# m = []
# for i in range(n):
#     m.append(list(map(int, input().split()[:n])))
    
# # def sum_glass(m, i, j):
# #     """Assumes hour-glass is in bounds of m!"""
# #     return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])

# # best = float("-inf")
# # for i in range(4):
# #     for j in range(4):
# #         s = sum_glass(m, i, j)
# #         if s > best:
# #             best = s
            
# # print (best)

def hourglassSum(m,i,j):
    return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = 6
    m = []
    for i in range(n):
        m.append(list(map(int,input().split()[:n])))
        
    best = float("-inf")
    for i in range(4):
        for j in range(4):
            s =  hourglassSum(m, i, j)
            if s > best:
                best = s
    print(best)

