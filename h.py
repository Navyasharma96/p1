import random
class A:
 def a1(self):
    a=random.randint(2,15)
    t=1
    mt=3
    win=False
    while t>mt:
        t+=1
        print("enter the no")
        b=input()
        if a==b:
            win=True
            print("you won")
            break
        elif a<b:
            print("your number is greater")
        else:
            print("your number is smaller")
d=A()
d.a1()
if win:
    print("you win the game in",t,"tries and number is",a)
    print("if you play more press 0 otherwise press 1")
    c=input()
    if c==0:
      d.a1()
            
