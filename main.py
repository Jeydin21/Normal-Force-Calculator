import os

def calculateNormalForce(mass, american):
    if(american == True):
        force = (float(mass) * 0.45359237) * 9.8 # Pounds to kilograms conversion
        return "Your normal force is " + str(round(force, 3)) + " N"
    else:
        force = float(mass) * 9.8
        return "Your normal force is " + str(round(force, 3)) + " N"
    
os.system("clear")
american = input("Are you American? (y/n) ")
if(american == "y"):
    print(calculateNormalForce(input("What is your weight in pounds?\n> "), True))
else: 
    print(calculateNormalForce(input("What is your weight in kilograms?\n> "), False))