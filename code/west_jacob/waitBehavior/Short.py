from west_jacob.waitBehavior.WaitBehavior import WaitBehavior


class Short(WaitBehavior):
    def __init__(self):
        WaitBehavior.__init__(self)

    def GetWait(self):
        return 1

