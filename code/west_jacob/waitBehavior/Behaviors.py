
def AdaptWait(peopleCount):
    if peopleCount < 10:
        return 1.0
    else:
        return 2.0

def ShortWait(peopleCount):
    return 1.0

def LongWait(peopleCount):
    return 2.0
