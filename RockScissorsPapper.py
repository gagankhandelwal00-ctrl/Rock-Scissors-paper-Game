import random
choices = ["Rock","Scissor","Paper"]
user_choices = input("Choose Rock ,Paper,Scissor: ")
computer_choice = random.choice(choices)
print(f"Computer choice:{computer_choice}")

if user_choices==computer_choice:
    print("Match is tie-up")
elif user_choices=="Rock" and computer_choice=="Scissor" or \
user_choices=="Paper" and computer_choice=="Rock" or \
user_choices=="Scissor" and computer_choice=="Paper":
    print("You won the match")
else:
    print("Computer won the match")