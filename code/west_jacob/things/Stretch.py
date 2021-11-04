from west_jacob.things.Thing import Thing


class Stretch(Thing):
    def __init__(self, name):
        Thing.__init__(self)
        self.name = name
        self.length = 0.3
        self.leftCars = []
        self.rightCars = []

    def __str__(self):
        status = "    Traveling Left: {}\n    Traveling Right: {}"
        right = ""
        left = ""
        if len(self.rightCars) > 0:
            for car in self.rightCars:
                right += "[ ID:{0:<4}{1} ]".format(car.id, car.loc)

        return status.format(left, right)

    def addRightCar(self, car):
        self.rightCars.append(car)

    def updateCars(self):
        for car in list(self.rightCars):
            loc = car.updateLocation()
            if loc >= 0.3:
                self.next.addCarRight(car)
                self.rightCars.remove(car)
