from west_jacob.things.Thing import Thing


class Station(Thing):
    def __init__(self, name):
        Thing.__init__()
        self.name = name
        self.people = 0

    def peopleOn(self, count):
        self.people += count

    def peopleOff(self, count):
        self.people -= count
