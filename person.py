# Ken Holm
# Purpose: Introduction to Object Oriented Programming
# The Person class
#
# Properties
#  Age: getAge(), setAge()
#  Job: getJob(), setJob()
#  Name: getName(), setName()
#  Rate: getRate()
#  Days: getDays()
#
# Methods
#  calculateCharge(hours)
#  updateRate(rate)
#


class Person:
    # Private properties
    __age: int = 0
    __rate: float = 10.0

    __job: str = ""
    __name: str = ""

    __days = ["Monday", "Tuesday", "Friday", "Saturday"]

    ##################################
    # Instantiate a copy of this class
    def __init__(self,
                 name="",
                 age=0,
                 job=""):

        # Set all our properties
        self.setName(name)
        self.setAge(age)
        self.setJob(job)

    #########################################
    # Getter and setter for the name property
    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        try:
            if name:
                self.__name = name

        except Exception as e:
            raise e

    ########################################
    # Getter and setter for the age property
    def getAge(self) -> int:
        return self.__age

    def setAge(self, age: int) -> None:
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
    def getRate(self) -> float:
        return self.__rate

    ########################################
    # Getter and setter for the job property
    def getJob(self) -> str:
        return self.__job

    def setJob(self, job: str) -> None:
        try:
            if job:
                self.__job = job

        except Exception as e:
            raise e

    #############
    # Update Rate
    def updateRate(self, rate: float) -> None:
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
    def getDays(self) -> list:
        return self.__days

    ###################
    # Calculate Charges
    def calculateCharge(self, hours: int = 0) -> float:
        try:
            return float(hours) * self.getRate()

        except Exception as e:
            raise e
