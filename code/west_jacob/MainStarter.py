# GRADING CHECKLIST
# 1. Initial Show system
# Menu working			    X
# Shows system properly	    X
#
# 2. Menu framework
# Prompts correct 		    X
# Invalid input working 	X
#
# 3. Add Car
# Able to add short car to one end		    X
# Car at station shows 					    X
# Car str overridden						X
#
# 4. One Short Car Update (one way)
# Car time starts and decreases properly					X
# Car can move to next stretch at the right time			X
# Car displays and moves forward correctly on stretch		X
# Car enters next station at correct time and location	    X
# Next station handles time and release properly			X
# Car reaches the end station properly					    X
# Display is correct and done with iterator**				X
#
# 5. One Long Car Update  (one way)
# Repeat of prior tier with long car ignoring iterator 	    X
# Strategy pattern used properly**						    X
#
# 6. Set people and Adapting (one way)
# Updates station on/off count properly					    X
# Updates short/long car people count properly			    X
# Update adapting car properly with strategy**			    X
#
# 7. Multi short/long car (one way) and station details
# Waiting list works properly at start					    X
# Waiting list works properly at later stations			    X
# Show station details working properly**					X
# Later added cars work									    X
#
# 8. One short car, round trip
# Able to return to cable at end							X
# Returns at correct speed to start 						X
# Multiple cycles permitted								    X
#
# 9. Stress test
# multiple, varied cars									    X
#
#
# Grading tags completes :  X

import sys

from west_jacob.Gondola import Gondola


def main():
    """
    Starting point for the application, takes in user input and executes methods on the Gondola class.

    """
    gondola = Gondola()
    menu = "\n" \
           "1) Show Gondola System\n" \
           "2) Add Car\n" \
           "3) Update with Debug Info\n" \
           "4) Set Station People\n" \
           "5) Show Station Details\n" \
           "0) Quit\n"

    choice = -1

    while choice != 0 and choice != '0':
        print(menu)
        choice = input("Choice:> ")

        # strips out blank lines in input
        while choice == '':
            choice = input()

        if choice == '1':
            gondola.printSystem()  # Show Gondola System
        elif choice == '2':
            gondola.addCar()  # Add Car
        elif choice == '3':
            gondola.update()  # Update With Debug Info
        elif choice == '4':
            gondola.setStationPeople()  # Set Station People
        elif choice == '5':
            gondola.printStationDetails()  # Show Station Details
        elif choice == '0':
            return  # Quit
        else:
            print('Invalid menu option')

    return

if __name__ == '__main__':
    main( )
