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