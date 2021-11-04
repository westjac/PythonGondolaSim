from west_jacob.things.Thing import Thing


class Stretch(Thing):
    """
    Stretch inherits thing and is used to hold cars traveling between stations.

    """
    def __init__(self, name):
        Thing.__init__(self)
        self.name = name
        self.length = 0.3
        self.leftCars = []
        self.rightCars = []

    def __str__(self):
        """
        Overrides the str function for the class. Outputs what cars, if any, are traveling right and left on the stretch.

        :return: Cars traveling right and left on stretch
        """
        status = "    Traveling Left: {}\n    Traveling Right: {}"
        right = ""
        left = ""
        if len(self.rightCars) > 0:
            for car in self.rightCars:
                right += "[ ID:{0:<4}{1} ]".format(car.id, car.loc)
        if len(self.leftCars) > 0:
            for car in self.leftCars:
                left += "[ ID:{0:<4}{1} ]".format(car.id, car.loc)

        return status.format(left, right)

    def addRightCar(self, car):
        """
        Adds car going right.

        :param car: The car to add
        """
        self.rightCars.append(car)

    def addLeftCar(self, car):
        """
        Add car going left.

        :param car: The car to add
        """
        self.leftCars.append(car)

    def updateCars(self):
        """
        Updates the cars that are currently on the stretch. If they have moved the whole distance of the stretch,
        the cars are moved to the next station.

        """
        for car in list(self.rightCars):
            loc = car.updateLocation()
            if loc >= 0.3:
                self.next.addCarRight(car)
                self.rightCars.remove(car)

        for carLeft in list(self.leftCars):
            locLeft = carLeft.updateLocation()
            if locLeft >= 0.3:
                self.prev.addCarLeft(carLeft)
                self.leftCars.remove(carLeft)