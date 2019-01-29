def a1():
    import random
    a=random.randint(1,10)
    t=0
    mt=3
    while t<mt:
        t+=1
        guess=int(input("Guess a number"))
        if guess == a:
            print("you win")
            break
        elif guess>a:
          print("Sorry your number is greater")
        elif guess<a:
          print("Sorry number is lower")
        else:
            print("you loose the game")
    print("Press 0 of more play otherwise 1")
    c=int(input())
    if c==0:
        a1()
a1()

