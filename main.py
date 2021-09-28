# Ken Holm
# Purpose: Introduction the Object Oriented Programming
#  See https://docs.python.org/3/tutorial/classes.html

# Import our person class
from person import Person

###############################################
# Instantiate a Person object
###############################################
try:
    # Alex
    alex = Person("Alex", 12, "Lawn Care Tech")
    alex.updateRate(15.00)

    # Hannah
    # Now, instantiating a Person object with no information initially.
    #  Then adding that information after the object has been created.
    hannah = Person()
    hannah.setName("Hannah")
    hannah.setAge(15)
    hannah.setJob("Baker")
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

    print(f"My name is {hannah.getName()}.  My rate is ${hannah.getRate():#.2f} and I am a {hannah.getAge()} year old {hannah.getJob()}.")
    input("Press [ENTER] to continue ")
    print()

except Exception as e:
    print(f"Got an error: {e}")
