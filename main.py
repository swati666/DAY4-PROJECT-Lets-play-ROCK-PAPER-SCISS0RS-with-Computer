import random

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

# Write your code below this line 👇
loop = False
ask = ''
while not loop:
    humanPlayer = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    if humanPlayer == 0:
        print(rock)

    elif humanPlayer == 1:
        print(paper)

    elif humanPlayer == 2:
        print(scissors)

    computer_chose = random.randint(0, 2)
    print("Computer chose: ")
    if computer_chose == 0:
        print(rock)

    elif computer_chose == 1:
        print(paper)

    elif computer_chose == 2:
        print(scissors)

    if humanPlayer == 0 and computer_chose == 1:
        print("You Win!")
    elif humanPlayer == 1 and computer_chose == 0:
        print("You Win!")
    elif humanPlayer == 2 and computer_chose == 1:
        print("You Win!")
    elif humanPlayer == computer_chose:
        print("It's a Draw")
    else:
        print("You lose")

    ask = input("\n\n Do you want to continue with the GAME without scrating your head ;) ? type yes or no\n").lower()
    if ask == 'yes':
        loop = False
    else:
        loop = True