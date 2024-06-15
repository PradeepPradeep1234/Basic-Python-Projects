import random
comp_number=random.randint(1,100)
while(True):
    user_guess=int(input("enter a number to guess:"))
    if(user_guess==comp_number):
        print("you guessed it right 👍")
        break
    elif(user_guess>comp_number):
        print("Too high,try again 😜")
    else:
        print("Too low,try again 😜")
        