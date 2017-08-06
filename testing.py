def start():
    instructions = ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']
    grid = [['o', 'x', 'x'], ['x', 'o', '-'], ['x', '-', 'o']]
    gridcheck = []
    for i in range(len(grid)):
        print ('\n')
        for j in range(len(grid[i])):
            print(grid[i][j], end = '')


            # if "x" == (grid[i][j]) or "o" == (grid[i][j]):
            #    print('x', end=' ')

start()

