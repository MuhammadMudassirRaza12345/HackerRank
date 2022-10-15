 
    """ A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values. 
       Sample Code 
      
        >>> from collections import Counter 
        >>>  
        >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3] 
        >>> print Counter(myList) 
       Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1}) 
       >>> 
       >>> print Counter(myList).items() 
       [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)] 
       >>>  
       >>> print Counter(myList).keys() 
       [1, 2, 3, 4, 5] 
       >>>  
       >>> print Counter(myList).values() 
       [3, 4, 4, 2, 1] 
      
       Ali is a shoe shop owner. His shop has X  number of shoes. 
       He has a list containing the size of each shoe he has in his shop. 
       There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size. 
      
       Your task is to compute how much money Ali earned. 
      
       Input Format   
       The first line contains X, the number of shoes. 
       The second line contains the space separated list of all the shoe sizes in the shop. 
       The third line contains N, the number of customers. 
       The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe. 
      
       Output Format 
       Print the amount of money earned by Ali. 
      
       Sample Input 
       10 
       2 3 4 5 6 8 7 6 5 18 
       6 
       6 55   
       6 45 
       6 55 
       4 40 
       18 60 
       10 50 
      
       Sample Output 
       200 
      
       Explanation 
       Customer 1: Purchased size 6 shoe for $55. 
       Customer 2: Purchased size 6 shoe for $45. 
       Customer 3: Size 6 no longer available, so no purchase. 
       Customer 4: Purchased size 4 shoe for $40. 
       Customer 5: Purchased size 18 shoe for $60. 
       Customer 6: Size 10 not available, so no purchase. 
      
       Total money earned = 55+45+40+60 = 200 
      
       Enter your code here. Read input from STDIN. Print output to STDOUT 
       """
import collections 
from collections import Counter 
X = int(input()) 
shoe_sizes = Counter(map(int, input().split()))  
print(shoe_sizes) 
N = int(input()) 
earnings = 0 
for i in range(N): 
    size, price = map(int, input().split())
    if shoe_sizes[size]: 
        earnings += price 
        shoe_sizes[size] -= 1 
        print(earnings) 
     
