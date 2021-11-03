from west_jacob.waitBehavior.WaitBehavior import WaitBehavior


class Adapt(WaitBehavior):
    def __init__(self):
        WaitBehavior.__init__()

    def GetWait(self, peopleCount):
        if peopleCount < 10:
            return 1
        else:
            return 2
