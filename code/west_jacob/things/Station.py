from west_jacob.things.Thing import Thing


class Station(Thing):
    def __init__(self, name):
        Thing.__init__(self)
        self.name = name
        self.people = 0

    def __str__(self):
        string = "--------" + self.name
        if len(self.leftCars) > 0:
            left = " Left: [ ID:{0}   {1:.1f}min {2}/20 ]({3})"
            string += left.format(self.leftCars[0].id, self.leftCars[0].timeToClose, self.leftCars[0].people, 0)
        if len(self.rightCars) > 0:
            right = " Right: [ ID:{0}   {1:.1f}min {2}/20 ]({3})"
            string += right.format(self.rightCars[0].id, self.rightCars[0].Wait(), self.rightCars[0].people, 0)

        return string

    def peopleOn(self, count):
        self.people += count

    def peopleOff(self, count):
        self.people -= count
