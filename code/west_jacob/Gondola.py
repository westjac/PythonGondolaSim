from west_jacob.Car import Car
from west_jacob.iterator.IteratorAll import AllIter
from west_jacob.iterator.IteratorStationOnly import StationIter
from west_jacob.iterator.IteratorStretchOnly import StretchIter
from west_jacob.things.Station import Station
from west_jacob.things.Stretch import Stretch
from west_jacob.waitBehavior.Behaviors import *


class Gondola:
    """
    Class containing all data and operations associated with the Gondola application.

    """
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
        """
        Gets an iterator for all things (stations and stretches) in the system.

        :return: Iterator of all things
        """
        return AllIter(self.things)

    def getStationIterator(self):
        """
        Gets an iterator for all stations in the system.

        :return: Iterator of stations
        """
        return StationIter(self.things)

    def getStretchIterator(self):
        """
        Gets an iterator for all stretches in the system.

        :return: Iterator of stretches
        """
        return StretchIter(self.things)

    def printSystem(self):
        """
        Prints out the current status of the Gondola system.

        """
        iter = self.getIterator()

        print('Time: ' + str(self.time) + ' min')
        for thing in iter: # GRADING: LOOP_ALL
            print(thing)

        return

    def addCar(self):
        """
        Adds a car to the start of the gondola system going right. User can choose the wait time functionality
        when creating the car.

        """
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
        """
        Prompts the user to enter the number of people that load and unload at each station.

        """
        try:
            for station in self.getStationIterator():
                print(station.name)
                on = int(input("    Getting on:> "))
                if on > 20 or on < 0:
                    raise ValueError
                off = int(input("    Getting off:> "))
                if off > 20 or off < 0:
                    raise ValueError
                station.gettingOn = on
                station.gettingOff = off
        except ValueError:
            print("Invalid Input")

    def printStationDetails(self):
        """
        Prints details about each station in the Gondola system.

        """
        stationIter = self.getStationIterator()

        for station in stationIter: # GRADING: LOOP_CAR
            print(station)
            print("    People getting on/off: {}/{}".format(station.gettingOn, station.gettingOff))
            print("    Delayed on...")
            leftSide = ""
            for car in station.rightWaiting:
                leftSide += "[ ID:{0:<4}{1} ] ".format(car.id, car.loc)
            print("      Left Side: {}".format(leftSide))
            print("      Right Side: ")
            print("")

        return

    def update(self):
        """
        Iterates through the stations and stretches, updating the status and locations of all the cars.

        """
        self.time += 0.5
        for station in self.getStationIterator():
            station.updateCars()

        for stretch in self.getStretchIterator():
            stretch.updateCars()

        self.printSystem()
