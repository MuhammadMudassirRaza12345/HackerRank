# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be  N x M. (N is an odd natural number, and  M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

 



# Designer Door Mat in Python - HackerRank Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Designer Door Mat in Python - HackerRank Solution START
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))