# Guessing game

#Import random module
import random

#Set initial score to 0
score = 0

#Loop until score <10
while score<5:
    #User input
    userChoice = int(input("Enter a number from 1 to 10:"))
    #Random number generating
    randomNumber = random.randint(1,10)
    
    #Condition
    if(userChoice == randomNumber):
        print("You got it!🥰")
        #If true increase score
        score += 1
        print("Your score is:",score)
    else:
        print("Oh you miss the number!🥲")
        print("The number is:",randomNumber)
        
#If score is 10 stop the loop and print this 
print("Congrated!You got the number 5 Times!")
