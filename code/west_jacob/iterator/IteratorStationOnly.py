class StationIter:
    def __init__(self, things):
        self.things = things

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        try:
            # if thing is not a station, keep incrementing the index until it is
            self.index += 1
            return self.things[self.index]
        except:
            raise StopIteration()
