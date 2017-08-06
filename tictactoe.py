def start():
    instructions = ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']
    grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    gridcheck = []
    printInstructions(instructions)
    printGrid(grid)
    player1ltr = input('Player 1, do you want to be "x" or "o"?')
    if player1ltr == 'x':
        player1ltr = 'x'
        player2ltr = 'o'
    else:
        player2ltr = 'x'
        player1ltr = 'o'
    letters = player1ltr,player2ltr
    insertCheckIfExist(grid, gridcheck)
    player1go(letters, grid, gridcheck)

def printInstructions(instructions):
    for i in range(len(instructions)):
        print ('\n')
        for j in range(len(instructions[i])):
            print(instructions[i][j], end=' ')

def printGrid(grid):
    for i in range(len(grid)):
        print ('\n')
        for j in range(len(grid[i])):
            print(grid[i][j], end = '  ')
    print('\n')

def insertCheckIfExist (grid, gridcheck):
    if grid[0][0]+grid[0][1]+grid[0][2] == 'xxx' or grid[0][0]+grid[0][1]+grid[0][2] == 'ooo':
        print("You win")
        start()
    elif  grid[1][0]+grid[1][1]+grid[1][2] == 'xxx' or grid[1][0]+grid[1][1]+grid[1][2]== 'ooo':
        print("You win")
        start()
    elif  grid[2][0]+grid[2][1]+grid[2][2] == 'xxx' or grid[2][0]+grid[2][1]+grid[2][2] == 'ooo':
        print("You win")
        start()
    elif grid[0][0]+grid[1][1]+grid[2][2] == 'xxx' or grid[0][0]+grid[1][1]+grid[2][2]=='ooo':
        print("You win")
        start()
    elif  grid[0][2]+grid[1][1]+grid[2][0] == 'xxx' or grid[0][2]+grid[1][1]+grid[2][0]=='ooo':
        print("You win")
        start()
    elif  grid[0][0]+grid[1][0]+grid[2][0] == 'xxx' or grid[0][0]+grid[1][0]+grid[2][0]=='ooo':
        print("You win")
        start()
    elif  grid[0][1]+grid[1][1]+grid[2][1] == 'xxx' or grid[0][1]+grid[1][1]+grid[2][1]== 'ooo':
        print("You win")
        start()
    elif  grid[0][2]+grid[1][2]+grid[2][2] == 'xxx' or grid[0][2]+grid[1][2]+grid[2][2]=='ooo':
        print("You win")
        start()
    else:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if "x" == (grid[i][j]) or "o" == (grid[i][j]):
                    gridcheck.append(str(i)+str(j))

# def checkIfWin():
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if "x" == (grid[i][j]) or "o" == (grid[i][j]):
#     if (grid[][] == 'xxx')

def player1go(letters, grid, gridcheck):
        player1coord = str(input("Player 1, Please enter a coordinate(EX: b2): \n"))
        print ("you entered " + str(player1coord))

        if (player1coord[0] == "a"):
            player1row = 0
        elif (player1coord[0] == "b"):
            player1row = 1
        elif (player1coord[0] == "c"):
            player1row = 2
        if (player1coord[1] == "1"):
            player1column = 0
        elif (player1coord[1] == "2"):
            player1column = 1
        elif (player1coord[1] == "3"):
            player1column = 2
        insertCheckIfExist(grid, gridcheck)
        if (str(player1row) + str(player1column)) in gridcheck:
            print("Someone already placed a value here")
            player1go(letters, grid, gridcheck)
        else:
            grid[player1row][int(player1column)] = letters[0]
        insertCheckIfExist(grid, gridcheck)
        printGrid(grid)
        player2go(letters, grid, gridcheck)


def player2go(letters, grid, gridcheck):
    player2coord = str(input("Player 2, Please enter a coordinate(EX: b2): \n"))
    print("you entered " + str(player2coord))

    if (player2coord[0] == "a"):
        player2row = 0
    elif (player2coord[0] == "b"):
        player2row = 1
    elif (player2coord[0] == "c"):
        player2row = 2
    if (player2coord[1] == "1"):
        player2column = 0
    elif (player2coord[1] == "2"):
        player2column = 1
    elif (player2coord[1] == "3"):
        player2column = 2
    insertCheckIfExist(grid, gridcheck)
    if (str(player2row) + str(player2column)) in gridcheck:
        print("Someone already placed a value here")
        player2go(letters, grid, gridcheck)
    else:
        grid[player2row][int(player2column)] = letters[1]
    insertCheckIfExist(grid, gridcheck)
    printGrid(grid)
    player1go(letters, grid, gridcheck)

start()
