import random
from unittest import case


def game()
    {
        print("Select\nrock\npaper\nscissors")
        a=input()
        int b=char(a)
        l=[r,s,p]
        c=random.shuffle(l)
        if b==char(c):
            print("Draw")
        elif b<char(c):
            print("You lose")

    }
print("Do you want to play rock paper and scissors?")
a=input()
if a=='y':
    {
        game()
    }
else
    {
        print("Thank you")
    }