# Ken Holm
# Purpose: Introduction to Object Oriented Programming
# The Person class
#
# Properties
#  Age: getAge(), setAge()
#  Job: getJob(), setJob()
#  Name: getName(), setName()
#  Rate: getRate()
#  Days: getDays() # Days available
#
# Methods
#  calculateCharge(hours)
#  updateRate(rate)
#


class Person:
    # Private properties
    __age = 0
    __rate = 10.0

    __job = ""
    __name = ""

    __days = ["Monday", "Tuesday", "Friday", "Saturday"]

    # Class instantiator
    def __init__(self,
                 name="",
                 age=0,
                 job=""):

        # Set all our properties
        self.setName(name)
        self.setAge(age)
        self.setJob(job)

    # Getter and setter for the name property
    def getName(self):
        return (self.__name)

    def setName(self, name):
        try:
            if name:
                self.__name = name

        except Exception as e:
            raise e

    # Getter and setter for the age property
    def getAge(self):
        return (self.__age)

    def setAge(self, age):
        try:
            age = int(age)
        except Exception as e:
            raise e

        try:
            if age:
                self.__age = age

        except Exception:
            raise e

    # Getter and setter for the age property
    def getRate(self):
        return (self.__rate)

    # Getter and setter for the job property
    def getJob(self):
        return (self.__job)

    def setJob(self, job):
        try:
            if job:
                self.__job = job
        except Exception as e:
            raise e

    #############
    # Update Rate
    def updateRate(self, rate):
        try:
            rate = float(rate)
        except Exception as e:
            raise e

        try:
            if rate:
                self.__rate = rate

        except Exception:
            raise e

    ##########
    # Get Days
    def getDays(self):
        return (self.__days)

    ###################
    # Calculate Charges
    def calculateCharge(self, hours=0):
        try:
            hours = float(hours)
            return hours * self.getRate()

        except Exception as e:
            raise e


