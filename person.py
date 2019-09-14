# Ken Holm
# Purpose: Introduction to Object Oriented Programming
# The Person class
#
# Properties
#  Age: getage(), setage()
#  Job: getjob(), setjob()
#  Name: getname(), setname()
#  Rate: getrate()
#  Days: getdays()
#
# Methods
#  calculatecharge(hours)
#  updaterate(rate)
#


class Person:
    # Private properties
    __age = 0
    __rate = 10.0

    __job = ""
    __name = ""

    __days = ["Monday", "Tuesday", "Friday", "Saturday"]

    ####################
    # Class instantiator
    def __init__(self,
                 name="",
                 age=0,
                 job=""):

        # Set all our properties
        self.setname(name)
        self.setage(age)
        self.setjob(job)

    #########################################
    # Getter and setter for the name property
    def getname(self):
        return self.__name

    def setname(self, name):
        try:
            if name:
                self.__name = name

        except Exception as e:
            raise e

    ########################################
    # Getter and setter for the age property
    def getage(self):
        return self.__age

    def setage(self, age):
        try:
            age = int(age)
        except Exception as e:
            raise e

        try:
            if age:
                self.__age = age

        except Exception as e:
            raise e

    #############################
    # Getter for the age property
    def getrate(self):
        return self.__rate

    ########################################
    # Getter and setter for the job property
    def getjob(self):
        return self.__job

    def setjob(self, job):
        try:
            if job:
                self.__job = job

        except Exception as e:
            raise e

    #############
    # Update Rate
    def updaterate(self, rate):
        try:
            rate = float(rate)

        except Exception as e:
            raise e

        try:
            if rate:
                self.__rate = rate

        except Exception as e:
            raise e

    ##########
    # Get Days
    def getdays(self):
        return self.__days

    ###################
    # Calculate Charges
    def calculatecharge(self, hours=0):
        try:
            return float(hours) * self.getrate()

        except Exception as e:
            raise e
