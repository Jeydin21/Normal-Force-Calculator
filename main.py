import os

def calculateNormalForce(mass, shit):
    mass = float(mass)  # Typecast mass to double
    if(shit == False):
        force = (mass * 0.45359237) * 9.8
        return "Your normal force is " + str(round(force, 3)) + " N"
    else:
        force = mass * 9.8
        return "Your normal force is " + str(round(force, 3)) + " N"
    
os.system("clear")
american = input("Are you American? (y/n) ")
if(american == "y"):
    shit = False
    weight = input("What is your weight in pounds? ")
    print(calculateNormalForce(weight, shit))
else: 
    shit = True
    weight = input("What is your weight in kilograms? ")
    print(calculateNormalForce(weight, shit))



