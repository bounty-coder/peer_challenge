# John and Joe are playing the game. Initially, they have a string of length consisting of 0's and 1's only.
#  Both the players are playing game optimally taing alternate turns.

# In each turn, the player removes only one occurence of either substring '01' or '10' from anywhere in the given binary string.

#  The player who cannot make a move loses the game.
#  If John makes the first move, he wonders who will win the game.
#  You, being his friend, help him solve his problem.



def final(s,n):
    x,y=0,0
    for i in range(n):
        if s[i]=='1':
            x+=1
        else:
            y+=1
    m=min(x,y)
    if m%2==0:
        print("Joe")
    else:
        print("John")

t=int(input())
while t:
    n=int(input())
    s=input()
    final(s,n)
    t-=1