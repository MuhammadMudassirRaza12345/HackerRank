"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array[1,2,3,4,5] , then the array would become [3,4,5,1,2] .
Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
Given an array a of n integers and a number, d , perform d left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

int a[n]: the array to rotate
int d: the number of rotations
Returns

int a'[n]: the rotated array

Input Format

The first line contains two space-separated integers n and d , the size of a and the number of left rotations
The second line contains n space-separated integers, each an a[i] .
Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4 





"""
def rotLeft(n,a, d):
   arr=[]
   for i in range(d,n):
     arr.append(a[i])
   
   i = 0
   for i in range (0,d):
     arr.append(a[i])
   a=arr.copy()
   return a
     
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    # length of array
    n = int(first_multiple_input[0])
    #no of left rotations 
    d = int(first_multiple_input[1])
    a = list(map(int, input().rstrip().split()))
    results=rotLeft(n,a, d) 
    for i,result in enumerate(results):
        print(result,end=" ")
    
     
     