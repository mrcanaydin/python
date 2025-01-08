import random
graphRock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

graphPaper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

graphScissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input("Pick one: Rock, Paper, Scissors")
selection = ["Rock", "Paper", "Scissors"]
computer = random.choice(selection)
if user == "Rock":
    print(graphRock)
    if computer == "Rock":
        print(f"Draw, Computer chose \n {graphRock}")
    elif computer == "Paper":
        print(f"You Loose, Computer chose \n {graphPaper}")
    else:
        print(f"You Win, Computer chose \n {graphScissors}")
elif user == "Paper":
    print(graphPaper)
    if computer == "Rock":
        print(f"You Win, Computer chose \n {graphRock}")
    elif computer == "Paper":
        print(f", Computer chose \n {graphPaper}")
    else:
        print(f"You Loose, Computer chose \n {graphScissors}")
elif user == "Scissors":
    print(graphScissors)
    if computer == "Rock":
        print(f"You Loose, Computer chose \n {graphRock}")
    elif computer == "Paper":
        print(f"You Win, Computer chose \n {graphPaper}")
    else:
        print(f"Draw, Computer chose \n {graphScissors}")
