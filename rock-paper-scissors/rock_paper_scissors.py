rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors \n"))

game_images = [rock,paper,scissors]
if choice >=3 or choice < 0:
  print("Invalid choice, You lose.")
else:
 print(game_images[choice])



 import random
 computer_choice = random.randint(0, 2)
 print("Computer choice:")
 print(game_images[computer_choice])



 if choice == 0 and computer_choice == 2 :
  print("You win")
 elif (choice == 2 and computer_choice  == 1):
  print("You win")
 elif (choice == 1 and computer_choice == 0):
  print("You win")
 elif choice == computer_choice:
  print("It's a draw")
 else:
  print(" You lose")
