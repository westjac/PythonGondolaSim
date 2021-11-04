
class Thing:
    """
    The thing class primaraly assists in building the linked list for the things. This helps with moving cars from
    one thing to another in the gondola system.

    """
    def __init__(self, nextThing=None, prevThing=None):
        self.name = ''
        self.next = nextThing
        self.prev = prevThing

    def setNext(self, nextThing):
        """
        Sets the next item in the linked list.

        :param nextThing: The next thing
        """
        self.next = nextThing

    def setPrev(self, prevThing):
        """
        Sets the previous item in the linked list.

        :param prevThing: The previous thing
        """
        self.prev = prevThing
