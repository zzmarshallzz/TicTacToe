#Variables
instructions=['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3']
grid = ['-','-','-'],['-','-','-'],['-','-','-']
gridcheck = []
Player1ltr = None
Player2ltr = None

def printInstructions():
    for xs in instructions:
        print(" ".join(map(str, xs)))

def printGrid():
    for xs in grid:
        print(" ".join(map(str, xs)))

def start():
    global Player1ltr
    global Player2ltr
    printInstructions()
    printGrid()
    Player1ltr = input('Player 1, do you want to be "x" or "o"?')
    if Player1ltr == 'x':
        Player1ltr = 'x'
        Player2ltr ='o'
    else:
        Player2ltr = 'x'
        Player1ltr = 'o'
    Player1go()

def insertCheckIfExist():
    global gridcheck
    global grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if "x" == (grid[i][j]) or "o" == (grid[i][j]):
                gridcheck.append(str(i)+str(j))


def checkIfWin():
    if

def Player1go():
        Player1row = str(input("Player 1, Please enter a row position(a,b or c): \n"))
        print ("you entered " + str(Player1row))
        Player1column = int(input("Player 1, Please enter a column (1,2 or 3) \n"))
        print ("you entered " + str(Player1column))
        if (Player1row == "a"):
            Player1row = 0
        elif (Player1row == "b"):
            Player1row = 1
        elif (Player1row == "c"):
            Player1row = 2
        insertCheckIfExist()
        if (str(Player1row) + str(Player1column-1)) in gridcheck:
            print("Someone already placed a value here")
            Player1go()
        else:
            grid[Player1row][Player1column-1] = Player1ltr
        printGrid()
        print(gridcheck)
        Player2go()


def Player2go():
    Player2row = str(input("Player 2, Please enter a row position(a,b or c): \n"))
    print("you entered " + str(Player2row))
    Player2column = int(input("Player 2, Please enter a column (1,2 or 3) \n"))
    print("you entered " + str(Player2column))
    if (Player2row == "a"):
        Player2row = 0
    elif (Player2row == "b"):
        Player2row = 1
    elif (Player2row == "c"):
        Player1row = 2
    insertCheckIfExist()
    if (str(Player2row) + str(Player2column-1)) in gridcheck:
        print("Someone already placed a value here")
        Player2go()
    else:
        grid[Player2row][Player2column - 1] = Player2ltr
    printGrid()
    Player1go()

start()
