from west_jacob.things.Thing import Thing


class Stretch(Thing):
    def __init__(self, length):
        Thing.__init__()
        self.length = length