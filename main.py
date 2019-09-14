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
    alex.updateRate(15.00)

    # Hannah
    hannah = Person("Hannah", 13, "Baker")
    hannah.updateRate(40.00)

    hours = 10

    print(f"My name is {alex.getName()}")
    print(f"My age is {alex.getAge()}")
    print(f"My job is {alex.getJob()}")
    print(f"I am available on {', '.join(alex.getDays())}")
    print(f"For {int(hours):#.2f} hours @ a rate of ${alex.getRate():#.2f} per hour, the total is ${alex.calculateCharge(hours):#.2f}")
    input("Press [ENTER] to continue ")
    print()

    # Increase the rate
    alex.updateRate(float(input("What is the new rate? ")))

    # Update the number of hours
    hours = input("How many hours? ")

    print(f"My new Rate is {alex.getRate():#.2f}")
    print(f"For {int(hours):#.2f} hours @ a rate of ${alex.getRate():#.2f} per hour, the total is ${alex.calculateCharge(hours):#.2f}")
    input("Press [ENTER] to continue ")
    print()

    print(f"My name is {hannah.getName()}.  My rate is ${hannah.getRate():#.2f}")
    input("Press [ENTER] to continue ")
    print()

except Exception as e:
    print(f"Got an error: {e}")
