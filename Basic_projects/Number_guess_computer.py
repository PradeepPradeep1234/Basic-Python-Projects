import random
user_num=int(input("enter a number to guess:"))
feedback=""
low=10
high=30
chance=1
while (feedback!="c"):
    computer_guess=random.randint(low,high)
    print(f" computer guess:{computer_guess}")
    feedback=input("whether it is (low='l') or (high='h') or (correct='c')")
    if(feedback=="l"):
        low=computer_guess+1
        chance+=1
    elif(feedback=="h"):
        high=computer_guess-1
        chance+=1
    elif(feedback!='c' or 'l' or 'h'):
        print("Invalid option")
print(f"You guessed it at {chance} try  👍")
