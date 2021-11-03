from west_jacob.Car import Car
from west_jacob.iterator.IteratorAll import AllIter
from west_jacob.iterator.IteratorStationOnly import StationIter
from west_jacob.things.Station import Station
from west_jacob.things.Stretch import Stretch
from west_jacob.waitBehavior.Adapt import Adapt
from west_jacob.waitBehavior.Long import Long
from west_jacob.waitBehavior.Short import Short


class Gondola:
    def __init__(self):
        self.time = 0
        self.idCount = 1
        start = Station("Start")
        stretch1 = Stretch("Stretch 1")
        stationA = Station("Station A")
        stretch2 = Stretch("Stretch 2")
        stationB = Station("Station B")
        stretch3 = Stretch("Stretch 3")
        end = Station("End")
        self.things = [start, stretch1, stationA, stretch2, stationB, stretch3, end]

        # Set Linked List
        start.setPrev(stretch1)
        start.setNext(stretch1)
        stretch1.setPrev(start)
        stretch1.setNext(stationA)
        stationA.setPrev(stretch1)
        stationA.setNext(stretch2)
        stretch2.setPrev(stationA)
        stretch2.setNext(stationB)
        stationB.setPrev(stretch2)
        stationB.setNext(stretch3)
        stretch3.setPrev(stationB)
        stretch3.setNext(end)
        end.setPrev(stretch3)
        end.setNext(stretch3)

        # Set starting point of list for class
        self.start = start

    def getIterator(self):
        return AllIter(self.things)

    def getStationIterator(self):
        return StationIter(self.start)  # TODO: implement stations only

    def printSystem(self):
        iter = self.getIterator()

        print('Time: ' + str(self.time) + ' min')
        for thing in iter:
            print(thing)

        return

    def addCar(self):
        carType = input("Which type: 0-->Short, 1-->Long, 2-->Adapting:> ")

        newCar = Car(self.idCount)
        self.idCount += 1

        if carType == '0':
            newCar.SetWait(Short())
        elif carType == '1':
            newCar.SetWait(Long())
        elif carType == '2':
            newCar.SetWait(Adapt())
        else:
            print("Invalid Input")

        self.things[0].addCar(newCar) # Add Car to Start
        return

    def setStationPeople(self):
        try:
            print("Start")
            startOn = int(input("    Getting on:> "))
            if startOn > 20 or startOn < 0:
                raise ValueError
            startOff = int(input("    Getting off:> "))
            if startOff > 20 or startOff < 0:
                raise ValueError
        except ValueError:
            print("Invalid Input")
