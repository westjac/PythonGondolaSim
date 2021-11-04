class Car:
    """
    Car class representing the cars in the gondola system.

    """
    def __init__(self, id):
        self.id = id
        self.people = 0
        self.timeToClose = 0.0
        self.loc = 0.0
        self.waitBehavior = None

    def SetWait(self, waitBehavior):  # GRADING: SET_BEHAVIOR
        """
        Sets the wait behavior after the car class is instantiated

        :param waitBehavior: A function defining the wait time
        """
        self.waitBehavior = waitBehavior

    def Wait(self):  # GRADING: USE_BEHAVIOR
        """
        Function that executes the wait behavior set by the SetWait function.

        """
        if self.waitBehavior is not None:
            self.timeToClose = self.waitBehavior(self.people)

    def updateWait(self):
        """
        When called, decrements the time to close by 0.5 of a minute on the car.

        :return: Time left before the car doors close.
        """
        self.timeToClose -= 0.5
        return self.timeToClose

    def resetLocation(self):
        """
        Resets the car's location to zero.

        """
        self.loc = 0.0
        return

    def updateLocation(self):
        """
        Increments the car's location by 0.1 miles.

        :return: The cars current location
        """
        self.loc += 0.1
        return self.loc

    def updatePeople(self, people):
        """
        updates the number of people in the car. Has a hard boundary of 0-20 people. if you go over or under
        the min and max values will be used in it's place.

        """
        if self.people + people < 0:
            self.people = 0
        elif self.people + people > 20:
            self.people = 20
        else:
            self.people += people
        return
