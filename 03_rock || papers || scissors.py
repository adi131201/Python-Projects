import random

userW, compW = 0,0
opt = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock, Paper or Scissors or Q to quit: ").lower()

    if user_input == 'q': break

    if user_input not in opt:
        continue

    randNum = random.randint(0,2)
    compChoice = opt[randNum]
    print("Computer picked",compChoice)

    if (user_input == 'rock' and compChoice == 'scissors') or (user_input == 'scissors' and compChoice == 'paper') or (user_input == 'paper' and compChoice == 'rock'):
        print("You won!")
        userW+=1
    
    elif user_input == compChoice:
        print("It's a draw!")
    
    else:
        print("Computer won!")
        compW+=1
        
print("Your Score:",userW)
print("Computer Score:",compW)

