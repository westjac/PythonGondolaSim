class AllIter:
    """
    Iterator that goes through all things in the gondola system.

    """
    def __init__(self, things):
        self.things = things

    def __iter__(self):  # GRADING: INTER_ALL
        self.index = -1
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.things[self.index]
        except:
            raise StopIteration()
