
class Car:
    def __init__(self, id):
        self.id = id
        self.people = 0
        self.timeToClose = 0.0
        self.loc = 0.0
        self.waitBehavior = None

    def SetWait(self, waitBehavior):
        self.waitBehavior = waitBehavior

    def Wait(self):
        if self.waitBehavior is not None:
            self.timeToClose = self.waitBehavior(self.people)

    def updateWait(self):
        self.timeToClose -= 0.5
        return self.timeToClose

    def resetLocation(self):
        self.loc = 0.0
        return

    def updateLocation(self):
        self.loc += 0.1
        return self.loc

    def updatePeople(self, people):
        if self.people + people < 0:
            self.people = 0
        elif self.people + people > 20:
            self.people = 20
        else:
            self.people += people
        return
