# # # Kevin and Stuart want to play the ‘The Minion Game’.

# # # Game Rules

# # # Both players are given the same string, S.
# # # Both players have to make substrings using the letters of the string S.
# # # Stuart has to make words starting with consonants.
# # # Kevin has to make words starting with vowels.
# # # The game ends when both players have made all possible substrings.

# # # Scoring
# # # A player gets +1 point for each occurrence of the substring in the string S.

# # # For Example:
# # # String S = BANANA
# # # Kevin’s vowel beginning word = ANA
# # # Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# # # For better understanding, see the image below:


# # Your task is to determine the winner of the game and their score.

# # Function Description

# # Complete the minion_game in the editor below.

# # minion_game has the following parameters:

# # string string: the string to analyze
# # Prints

# # string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# # Input Format

# # A single line of input containing the string S.
# # Note: The string S will contain only uppercase letters: [A-Z].

# # Constraints
# # 0 < len(S) < 10^6

# Sample Input

# BANANA
# Sample Output

# Stuart 12
# Note :
# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

# 1 way:
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += (len(s) - i)  # Number of possible words left to right from a word of length n is always 
                                         # n + (n-1) + (n-2) +..1
        else:
            stuart_score += (len(s) - i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
       
    
if __name__ == '__main__':
    s = input()
    minion_game(s)






# 2 way
def minion_game(string):
    k=0
    s=0
    vowels="AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in vowels:
            k=k+len(string)-i
        else:
            s=s+len(string)-i    
    
    if k>s:
        print("Kevin",k)
    elif k==s:
        print("Draw")    
    else:
        print("Stuart",s)            



if __name__ == '__main__':
    s = input()
    minion_game(s)
                       





# 3 way
 
# The Minion Game in Python - Hacker Rank Solution
def minion_game(string):
    # your code goes here
    # The Minion Game in Python - Hacker Rank Solution START
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")
    # The Minion Game in Python - Hacker Rank Solution END

if __name__ == '__main__':
    s = input()
    minion_game(s)