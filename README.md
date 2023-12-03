# Weight-Normal-Force-Calculator
A quick thing I did in 5 minutes

```py
# import os
def calculateNormalForce(mass, shit):
    return "Your normal force is " + str(round((float(mass) * 0.45359237) * 9.8, 3)) + " N" if not shit else "Your normal force is " + str(round(float(mass) * 9.8, 3)) + " N"
    
# os.system("clear")
american = input("Are you American? (y/n) ")
print(calculateNormalForce(input("What is your weight in pounds? "), False) if american == "y" else calculateNormalForce(input("What is your weight in kilograms? "), True))
```