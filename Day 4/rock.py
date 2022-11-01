import random
from tkinter import END

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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if choice == 0:
    print(rock)
    
elif choice == 1:
    print(paper)
    
elif choice == 2:
    print(scissors)
    
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer chose:")
    print(rock)
    
elif computer_choice == 1:
    print("Computer chose:")
    print(paper)
    
elif computer_choice == 2:
    print("Computer chose:")
    print(scissors)
    

if choice == 0:
    if computer_choice == 2:
        print("You win")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("It was a tie")
elif choice == 1:
    if computer_choice == 2:
        print("You lose")
    elif computer_choice == 1:
        print("It was a tie")
    else:
        print("You win")
elif choice == 2:
    if computer_choice == 2:
        print("It was a tie")
    elif computer_choice == 1:
        print("You win")
    else:
        print("You lose")
elif choice >= 3:
    print("You typed an invalid number. You lose!")