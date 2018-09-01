''' STARTING OUT WITH PROGRAMMING LOGIC AND DESIGN:
    CHAPTER 4 - DECISION STRUCTURE AND BOOLEAN LOGIC
The Fast Freight Shipping Company charges the following rates:

Weight of Package                       Rate/Pound
2 lbs or less                           $1.10
Over 2 lbs but not more than 6 lbs      $2.20
Over 2 lbs but not more than 10 lbs     $3.70
Over 10 lbs                             $3.80

Design a program that asks the user to enter the weight of a package and then
displays the shipping charges.
'''

# Prompt
weight = float(input("Enter the weight of the package: "))

# Decision Statement
if weight <= 2:
    print("Rate/Pound: $1.10")
elif 2 < weight <= 6:
    print("Rate/Pound: $2.20")
elif 6 < weight <= 10:
    print("Rate/Pound: $3.70")
else:
    print("Rate/Pound: $3.80")