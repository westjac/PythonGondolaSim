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

if __name__ == '__main__':
    main( )