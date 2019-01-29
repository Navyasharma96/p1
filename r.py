import random
print("Welcom to a Guessing Game")
a=random.randint(1,10)
t=0
mt=3
win=False
while t<mt:
    t+=1
    guess=int(input("Guess a number"))
    if guess == a:
        win = True
        break
    elif guess>a:
        print("Sorry your number is greater")
    else:
        print("Sorry number is lower")


if win:
    print("Your gussed number is",a)
    print("And it only took you",t,"tries")
else:
    print("You loose the game")
    print("The random number is ",a)
