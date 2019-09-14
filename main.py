# Ken Holm
# Purpose: Introduction the Object Oriented Programming

# Import our person class
from person import Person

###############################################
# Instantiate a Person object
###############################################
try:
    # Alex
    alex = Person("Alex", 10, "Lawn Care Tech")
    alex.updaterate(15.00)

    # Hannah
    hannah = Person("Hannah", 13, "Baker")
    hannah.updaterate(40.00)

    hours = 10

    print(f"My name is {alex.getname()}")
    print(f"My age is {alex.getage()}")
    print(f"My job is {alex.getjob()}")
    print(f"I am available on {', '.join(alex.getdays())}")
    print(f"For {int(hours):#.2f} hours @ a rate of ${alex.getrate():#.2f} per hour, the total is ${alex.calculatecharge(hours):#.2f}")
    input("Press [ENTER] to continue ")
    print()

    # Increase the rate
    alex.updaterate(float(input("What is the new rate? ")))

    # Update the number of hours
    hours = input("How many hours? ")

    print(f"My new Rate is {alex.getrate():#.2f}")
    print(f"For {int(hours):#.2f} hours @ a rate of ${alex.getrate():#.2f} per hour, the total is ${alex.calculatecharge(hours):#.2f}")
    input("Press [ENTER] to continue ")
    print()

    print(f"My name is {hannah.getname()}.  My rate is ${hannah.getrate():#.2f} and I am a {hannah.getjob()}.")
    input("Press [ENTER] to continue ")
    print()

except Exception as e:
    print(f"Got an error: {e}")
