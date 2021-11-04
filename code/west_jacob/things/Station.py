from west_jacob.things.Thing import Thing


class Station(Thing):
    def __init__(self, name):
        Thing.__init__(self)
        self.name = name
        self.people = 0
        self.gettingOn = 0;
        self.gettingOff = 0
        self.leftCar = None
        self.leftWaiting = []
        self.rightCar = None
        self.rightWaiting = []

    def __str__(self):
        string = "--------%-10s" % (self.name)
        # if len(self.leftCars) > 0:
        #     left = " Left: [ ID:{0}   {1:1f}min {2}/20 ]({3})"
        #     string += left.format(str(self.leftCars[0].id), self.leftCars[0].timeToClose, str(self.leftCars[0].people), 0)
        if self.rightCar is not None:
            right = "Right: [ ID:{}   {}min {}/20 ]({})"
            string += right.format(str(self.rightCar.id), self.rightCar.timeToClose, str(self.rightCar.people), 0)

        return string

    def peopleOn(self, count):
        self.people += count
        return

    def peopleOff(self, count):
        self.people -= count
        return

    def updateCars(self):
        if self.rightCar is not None:
            timeRight = self.rightCar.updateWait()
            if timeRight == 0:
                self.rightCar.resetLocation()
                self.next.addRightCar(self.rightCar)
                self.rightCar = None
        elif self.leftCar is not None:
            timeLeft = self.leftCar.updateWait()

        return

    def addCarRight(self, car):
        if self.rightCar is None:
            self.rightCar = car
            self.rightCar.Wait()
            self.rightCar.updatePeople(-self.gettingOff)
            self.rightCar.updatePeople(self.gettingOn)
        else:
            self.rightWaiting.append(car)
        return
