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

#Write your code below this line 👇
# print(rock)


def rock_paper_scissors(a, b):
  if a == 0:
    print(rock)
    if b == 1:
      print(f"Computer chose:\n{paper}\nYou lose")
    elif b == 2:
      print(f"Computer chose:\n{scissors}\nYou win!")
    else:
      print(rock + "\nIt's a draw")
  elif a == 1:
    print(paper)
    if b == 0:
      print(f"Computer chose:\n{rock}\nYou win!")
    elif b == 2:
      print(f"Computer chose:\n{scissors}\nYou lose")
    else:
      print(paper + "\nIt's a draw")
  else:
    print(scissors)
    if b == 0:
       print(f"Computer chose:\n{rock}\nYou lose")
    elif b == 1:
       print(f"Computer chose:\n{paper}\nYou win!")
    else:
      print(scissors + "\nIt's a draw")
  return a, b 

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

random_value = random.randint(0, 2)

rock_paper_scissors(choice, random_value)

# print(random_value)


  
