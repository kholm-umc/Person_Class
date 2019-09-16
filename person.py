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
    __age: int = 0
    __rate: float = 10.0

    __job: str = ""
    __name: str = ""

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
    def getname(self) -> str:
        return self.__name

    def setname(self, name: str) -> None:
        try:
            if name:
                self.__name = name

        except Exception as e:
            raise e

    ########################################
    # Getter and setter for the age property
    def getage(self) -> int:
        return self.__age

    def setage(self, age: int) -> None:
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
    def getrate(self) -> float:
        return self.__rate

    ########################################
    # Getter and setter for the job property
    def getjob(self) -> str:
        return self.__job

    def setjob(self, job: str) -> None:
        try:
            if job:
                self.__job = job

        except Exception as e:
            raise e

    #############
    # Update Rate
    def updaterate(self, rate: float) -> None:
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
    def getdays(self) -> list:
        return self.__days

    ###################
    # Calculate Charges
    def calculatecharge(self, hours: int = 0) -> float:
        try:
            return float(hours) * self.getrate()

        except Exception as e:
            raise e
