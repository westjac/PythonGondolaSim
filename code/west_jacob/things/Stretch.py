from west_jacob.things.Thing import Thing


class Stretch(Thing):
    def __init__(self, name):
        Thing.__init__(self)
        self.name = name
        self.length = 0.3

    def __str__(self):
        return "    Traveling Left: \n    Traveling Right: "
