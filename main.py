import random 

print ("Winning rule of the Rock-Paper-Scissor game ar as follows: \n Same choice-> draw \n Rock vs paper->paper wins \n Rock vs scissor->Rock wins \n paper vs scissor->scissor wins \n")

while True:
   possible_actions = ["R", "P", "S"]
   user_choice = (input("User turn (R, P, S):"))
   if user_choice not in possible_actions:
      print("Invalid input! Try again!")
   computer_selection = random.choice(possible_actions)

   print("Computer choice is: " + computer_selection)
   print(user_choice + "  vs  " + computer_selection)

   if user_choice == computer_selection:
       print("Both players selected {user_choice}. It's a tie")
   elif user_choice == "R":
       if computer_selection == "S":
        print("Rock smashes scissors! You win!")
       else:
        print("Paper covers rock! You lose!")
   elif user_choice == "P":
       if computer_selection == "R":
        print ("Paper covers rock! You win")
       else:
        print("Scissors cuts paper! You lose!")
   elif user_choice == "S":
       if computer_selection == "P":
        print ("Scissors cuts paper! You win!")
       else:
        print("Rock smashes scissors! You lose")

   print("Do you want to play again? (Y/N)")
   ans = input()
   if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
