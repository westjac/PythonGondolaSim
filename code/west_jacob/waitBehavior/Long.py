from west_jacob.waitBehavior.WaitBehavior import WaitBehavior


class Long(WaitBehavior):
    def __init__(self):
        WaitBehavior.__init__()
        self.waitTime = 2

    def GetWait(self):
        return 2
