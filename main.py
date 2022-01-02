print("Welcome to my computer quiz!")
playing=input("Do you want to play?")
if playing!="yes":
    quit()
print("okey! Let's play:)")
score=0
answer = input("what does cpu stands for?")
if answer.lower()=="central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect")
answer = input("What does GPU stands for?")
if answer.lower()== "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")
answer = input("what does RAM stands for?")
if answer.lower()=="random acess memory":
    print("correct!")
    score += 1
else:
    print("Incorrect")
answer = input("PSU?")
if answer.lower()=="power supply unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")
answer=input("what does ROM stands for")
if answer.lower()=="readonly memory"
    print("correct")
    score+=1
else
    print("incorrect")
print("You got "+str(score)+" questions currect!")
