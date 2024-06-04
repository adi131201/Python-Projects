print("Welcome to my computer quiz.")

playing = input("Do you want to play the Computer Hardware quiz? ")

if playing.lower() !="yes":
    quit()

print("Okay! Let us play then...")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! \nThe correct answer is Central Processing Unit.")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! \nThe correct answer is Power Supply Unit")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! \nThe correct answer is Graphics Processing Unit")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! \nThe correct answer is Random Access Memory")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! \nThe correct answer is Read Only Memory")

answer = input("What does DIMM stands for? ")
if answer.lower() == "dual inline memory modules":
    print("Correct! ")
    score+=1
else:
    print("Incorrect! \nThe correct answer is Dual Inline Memory Modules")

print("\nResult! \nYou scored " + str(score) + " out of 6.")