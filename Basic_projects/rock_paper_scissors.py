#you can easily alter and reduce the no of lines in code,it is beginner friendly.
import random
options=["rock","paper","scissors"]
count_computer=0
count_user=0
while(True):
    comp_output=random.choice(options)
    user_input=input()
    if(comp_output=="rock" and user_input=="scissors" or comp_output=="paper" and user_input=="rock" or comp_output=="scissors" and user_input=="paper"  ):
        print( "computer choice:",comp_output,"computer wins")
        count_computer+=1
        if(count_computer==5): #if computer wins 5 times ,it won the game
            print("game over,computer win")
            break
        # you can change below code as above all fails it is considered that the user wins.
        #lines of code will reduce!!
    elif(comp_output=="rock" and user_input=="paper" or comp_output=="scissors" and user_input=="rock" or comp_output=="paper" and user_input=="scissors"):
        print("user choice:",user_input ,'\n',"computer choice:",comp_output,"user wins")
        count_user+=1
        if(count_user==5):#if user wins 5 times ,user won the game
            print("game over,user wins!")
            break
    elif(user_input==comp_output):
        print("Drawn!")
    else:
        print("Invalid choice by user,(choose between 'rock','paper','scissors')")



