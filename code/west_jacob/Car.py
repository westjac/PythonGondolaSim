
class Car:
    def __init__(self, id):
        self.id = id
        self.people = 0
        self.timeToClose = 0.0
        self.loc = "Not sure whats here yet"
        self.waitBehavior = None

    def SetWait(self, waitBehavior):
        self.waitBehavior = waitBehavior

    def Wait(self):
        if self.waitBehavior is not None:
            self.timeToClose = self.waitBehavior(self.people)

