
# GRADING CHECKLIST
# 1. Initial Show system
# Menu working			    ____
# Shows system properly	    ____
#
# 2. Menu framework
# Prompts correct 		    ____
# Invalid input working 	____
#
# 3. Add Car
# Able to add short car to one end		    ____
# Car at station shows 					    ____
# Car str overridden						____
#
# 4. One Short Car Update (one way)
# Car time starts and decreases properly					____
# Car can move to next stretch at the right time			____
# Car displays and moves forward correctly on stretch		____
# Car enters next station at correct time and location	    ____
# Next station handles time and release properly			____
# Car reaches the end station properly					    ____
# Display is correct and done with iterator**				____
#
# 5. One Long Car Update  (one way)
# Repeat of prior tier with long car ignoring iterator 	    ____
# Strategy pattern used properly**						    ____
#
# 6. Set people and Adapting (one way)
# Updates station on/off count properly					    ____
# Updates short/long car people count properly			    ____
# Update adapting car properly with strategy**			    ____
#
# 7. Multi short/long car (one way) and station details
# Waiting list works properly at start					    ____
# Waiting list works properly at later stations			    ____
# Show station details working properly**					____
# Later added cars work									    ____
#
# 8. One short car, round trip
# Able to return to cable at end							____
# Returns at correct speed to start 						____
# Multiple cycles permitted								    ____
#
# 9. Stress test
# multiple, varied cars									    ____
#
#
# Grading tags completes :  _________

import sys


def main():

    time = 0
    menu = "\n" \
           "1) Show Gondola System\n" \
           "2) Add Car\n" \
           "3) Update with Debug Info\n" \
           "4) Set Station People\n" \
           "5) Show Station Details\n" \
           "0) Quit\n"

    choice = -1
    while choice != 0 and choice != '0' :
        print( menu )
        choice = input( "Choice:> " )

        # strips out blank lines in input
        while choice == '':
            choice = input()

        if choice == '1':
            print('not implemented') # Show Gondola System
        elif choice == '2':
            print('not implemented') # Add Car
        elif choice == '3':
            print('not implemented') # Update With Debug Info
        elif choice == '4':
            print('not implemented') # Set Station People
        elif choice == '5':
            print('not implemented') # Show Station Details
        elif choice == '0':
            sys.exit() # Quit
        else:
            print('Invalid menu option')


if __name__ == '__main__':
    main( )