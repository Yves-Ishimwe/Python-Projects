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
import random
#Write your code below this line 👇
computer=[rock,paper,scissors]
choice1=input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n")
choice1=int(choice1)
computer_choice=random.randint(0,2)

if choice1 == 0:
  print("You chose:",rock)
  print(f"The computer chose {computer[computer_choice]}")
  if computer_choice == 0:
      print("it is a draw")
  elif computer_choice == 1:
      print("You loose")
  elif computer_choice == 2:
      print("You Win")
  
elif choice1 == 1:
  print("You chose:",paper)
  print(f"The computer chose {computer[computer_choice]}")
  if computer_choice == 1:
      print("it is a draw")
  elif computer_choice == 2:
      print("You loose")
  elif computer_choice == 0:
      print("You Win")
  
  
elif choice1 == 2:
  print("You chose:",scissors)
  print(f"The computer chose {computer[computer_choice]}")
  if computer_choice == 2:
      print("it is a draw")
  elif computer_choice == 0:
      print("You loose")
  elif computer_choice == 1:
      print("You Win")
else:
    print("You typed an invalid number. Choose either 0,1 or 2.")
  
