import random

print ("Welcome to Rock - Paper - Scissors Game!")

choices=["rock",'paper',"scissors"]

user_choice=input("choose rock, paper or scissors: ").lower()
computer_choice=random.choice(choices)

print("you chose: " , user_choice)
print("computer chose : " ,computer_choice)

if user_choice == computer_choice:
    print("it's a draw!")

elif(user_choice=="rock" and computer_choice == "scissors") or \
    (user_choice == "paper" and computer_choice=="rock") or \
    (user_choice =="scissors" and computer_choice=="paper"):
    print ("You Win :) ")
else:
    print("Computer Wins ! ")