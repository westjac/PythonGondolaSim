from west_jacob.Car import Car
from west_jacob.iterator.IteratorAll import AllIter
from west_jacob.iterator.IteratorStationOnly import StationIter
from west_jacob.iterator.IteratorStretchOnly import StretchIter
from west_jacob.things.Station import Station
from west_jacob.things.Stretch import Stretch
from west_jacob.waitBehavior.Behaviors import *


class Gondola:
    carId = 1

    def __init__(self):
        self.time = 0
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
        return StationIter(self.things)

    def getStretchIterator(self):
        return StretchIter(self.things)

    def printSystem(self):
        iter = self.getIterator()

        print('Time: ' + str(self.time) + ' min')
        for thing in iter:
            print(thing)

        return

    def addCar(self):
        carType = input("Which type: 0-->Short, 1-->Long, 2-->Adapting:> ")

        newCar = Car(Gondola.carId)

        if carType == '0':
            newCar.SetWait(ShortWait)
        elif carType == '1':
            newCar.SetWait(LongWait)
        elif carType == '2':
            newCar.SetWait(AdaptWait)
        else:
            print("Invalid Input")
            return

        newCar.Wait()
        self.things[0].addCarRight(newCar)  # Add Car to Start
        Gondola.carId += 1
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

    def update(self):
        self.time += 0.5
        for station in self.getStationIterator():
            station.updateCars()

        for stretch in self.getStretchIterator():
            stretch.updateCars()

        self.printSystem()
