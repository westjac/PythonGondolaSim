
class Thing:
    def __init__(self, nextThing=None, prevThing=None):
        self.name = ''
        self.next = nextThing
        self.prev = prevThing




    def setNext(self, nextThing):
        self.next = nextThing

    def setPrev(self, prevThing):
        self.prev = prevThing
