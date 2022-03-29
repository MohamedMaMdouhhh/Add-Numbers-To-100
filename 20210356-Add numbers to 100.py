while True:
    print("~~~~~ THE 100 GAME - CODED BY mohamed ~~~~~")
    print('----- MENU -----')
    print('1 - Start multiplayer game')
    print('2 - Quit game')
    choice = int(input('What are you going to do? Input the number representing your choice. '))
    if choice == 1:
        print("Let's do it!")
    elif choice == 2:
        print('See you soon.')
        break
    else:
        print('wrong choice please try again')
        print("~~~~~ THE 100 GAME - CODED BY mohamed ~~~~~")
        print('----- MENU -----')
        print('1 - Start multiplayer game')
        print('2 - Quit game')
        choice = int(input('What are you going to do? Input the number representing your choice. '))
        if choice == 1:
            print("Let's do it!")
        elif choice == 2:
            print('See you soon.')
            break
        else:
            print('wrong choice please try again')
    while True:
        print(' player 1, tell me your name:')
        oneName = input()
        print('Well then, player 2, what about you ?')
        twoName = input()
        print('Well there are, ' + oneName + ' and ' + twoName + ', and welcome to 100 game!')
        print('You will each take turns to choose a number between 1 and 10.')
        print('The first person to reach 100 is the winner.')
        print("Have fun, and let's get started!")
        totalNumber = 0
        while True:
            while totalNumber < 100:
                numberOne = input(oneName + ', give me a number between 1 and 10.')
                numberOne = int(numberOne)
                totalNumber += numberOne
                print("Got it, " + oneName + "! Below is the total right now:")
                print(totalNumber)
                if totalNumber == 100:
                    print(oneName, " won the game")
                break
            while totalNumber < 100:
                numberTwo = input(twoName + ', give me a number between 1 and 10.')
                numberTwo = int(numberTwo)
                totalNumber += numberTwo
                print("Got it, " + twoName + "! Below is the total right now:")
                print(totalNumber)
                if totalNumber == 100:
                    print(twoName, " won the game")
                break
