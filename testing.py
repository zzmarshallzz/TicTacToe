
grid = [['-','x','-'],['-','o','-'],['x','x','-']]


gridcheck = []

def checkIfExist():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if "x" == (grid[i][j]) or "o" == (grid[i][j]):
                gridcheck.append(str(i)+str(j))



checkIfExist()
print(grid)
print (gridcheck)