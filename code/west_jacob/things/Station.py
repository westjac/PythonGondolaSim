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
        if self.leftCar is not None:
            left = "Left: [ ID:{0:<4}{1}min {2}/20 ]({3})   "
            string += left.format(str(self.leftCar.id), self.leftCar.timeToClose, str(self.leftCar.people), len(self.leftWaiting))
        if self.rightCar is not None:
            right = "Right: [ ID:{0:<4}{1}min {2}/20 ]({3})"
            string += right.format(str(self.rightCar.id), self.rightCar.timeToClose, str(self.rightCar.people), len(self.rightWaiting))

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
            if timeRight == 0: # The gondola is ready to move to the next stretch
                self.rightCar.resetLocation()
                if self.name == "End": # Special Case for end station- loop around
                    self.next.addLeftCar(self.rightCar)
                else:
                    self.next.addRightCar(self.rightCar)
                self.rightCar = None

                if len(self.rightWaiting) > 0: # Check if there are any other gondolas waiting for the station
                    self.rightCar = self.rightWaiting.pop(0)
                    self.rightCar.updatePeople(-self.gettingOff)
                    self.rightCar.updatePeople(self.gettingOn)
                    self.rightCar.Wait()

        if self.leftCar is not None:
            timeLeft = self.leftCar.updateWait()
            if timeLeft == 0: # The gondola is ready to move to the next stretch
                self.leftCar.resetLocation()
                if self.name == "Start": # Special Case for start station- loop around
                    self.next.addRightCar(self.leftCar)
                else:
                    self.prev.addLeftCar(self.leftCar)
                self.leftCar = None

                if len(self.leftWaiting) > 0: # Check if there are any other gondolas waiting for the station
                    self.leftCar = self.leftWaiting.pop(0)
                    self.leftCar.updatePeople(-self.gettingOff)
                    self.leftCar.updatePeople(self.gettingOn)
                    self.leftCar.Wait()
        return

    def addCarRight(self, car):
        if self.rightCar is None:
            self.rightCar = car
            self.rightCar.updatePeople(-self.gettingOff)
            self.rightCar.updatePeople(self.gettingOn)
            self.rightCar.Wait()
        else:
            car.resetLocation()
            self.rightWaiting.append(car)
        return

    def addCarLeft(self, car):
        if self.leftCar is None:
            self.leftCar = car
            self.leftCar.updatePeople(-self.gettingOff)
            self.leftCar.updatePeople(self.gettingOn)
            self.leftCar.Wait()
        else:
            car.resetLocation()
            self.leftWaiting.append(car)
        return
