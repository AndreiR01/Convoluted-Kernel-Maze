from random import randint

#Function to build the maze with the 3 parameters.
def build_maze(m, n, swag):
    grid = []
    #2 nested for loops in order to create a 2D array(linked lists)
    for i in range(m):#iterates from 0-m creating the columns
        row = []
        for j in range(n):#iterates from 0-n creating the rows
            row.append("wall")
            #TO SEE HOW FOR LOOP WORKS UNCOMMENT AND CALL THE Function
            #print("i:" + str(i) +"and j:" + str(j))
            #print(row)
        grid.append(row)
    #print(grid)
    #creating random points to set 'start' to.
    start_i, start_j = randint(0, m - 1), randint(0, n - 1)
    grid[start_i][start_j] = 'starts'
    mow(grid, start_i, start_j)
    return grid

#Recursively function which randomly picks a direction to explore from the 'start' point. It moves 2 places in that direction and then if that place is a "wall" it will set the cell to empty. Also the cell connecting start and the empty cell is also set to empty so a path is emerged.
def mow(grid, i, j):
    #i - COLUMN index
    #j - ROW index
    directions  = ["U", "D", "L", "R"]
    while len(directions) > 0:
        directions_index = randint(0, len(directions) - 1) #-1 is used because the length of the list is one extra than the index of the last element of the list
        direction = directions.pop(directions_index)#return and pop idx of direction

        #following code looks if we can move in any direction
        if direction == "U": # when we travel UP the grid, our i(ROW) index decreases
            if i - 2 < 0: #if true we are ouside of bounds of our grid
                continue
            elif grid[i - 2][j] == "wall": #sets to empty if theres walls in the up direction
                grid[i - 2][j] == "empty"
                grid[i - 1][j] == "empty"
                mow(grid, i - 2, j) #recursively calling mow from  the place we just mowed

        elif direction == "D": #when we travel DOWN the grid, our i(ROW) index increases
            if i + 2 >= len(grid):#len looks at length of column
                continue
            elif grid[i + 2][j] == "wall": # sets to empty if theres a wall
                grid[i + 2][j] == "empty"
                grid[i + 1][j] == "empty"
                mow(grid, i + 2, j) #recursively calling mow from  the place we just mowed

        elif direction == "L": #when we travel LEFT the grid, our j(COLUMN) index decreases
            if j - 2 < 0:
                continue
            elif grid[i][j - 2] == "wall":
                grid[i][j - 2] == "empty"
                grid[i][j - 1] == "empty"
                mow(grid, i, j - 2) #recursively calling mow from  the place we just mowed

        else:# going RIGHT
            if j + 2 >= len(grid[0]):#len looks at length of ROWS
                continue
            elif grid[i][j + 2] == "wall":
                grid[i][j + 2] == "empty"
                grid[i][j + 2] == "empty"
                mow(grid, i, j + 2) #recursively calling mow from  the place we just mowed


#function takes care of printing the maze
def print_maze(grid):
    for row in grid:
        printable_row = ''
        for cell in row:
            if cell == "wall":
                char = '|'
            elif cell == "start":
                char = "X"
            else:
                char = " "
            printable_row += char
        print(printable_row)

#print(build_maze(2, 4, None))
print_maze(build_maze(3, 4, None))
