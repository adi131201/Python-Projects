import random

num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    if num<=0:
        print("Enter a number greater then 0 next time.")
        quit()
else:
    print("Please! Enter a number.")
    quit()

randNum = random.randint(0,num)
guesses = 0
while True:
    guesses+=1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Enter a number next time.')
        continue

    if guess==randNum:
        print('Yay! You guessed it!')
        break
    
    elif guess>randNum:
        print("You were above the number.")
    
    else:
        print("You were below the number.")

print("You guessed in", guesses, "guesses.")