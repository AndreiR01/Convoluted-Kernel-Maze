from random import randint

def build_maze(m, n, swag):
    grid = []
    #2 nested for loops in order to create a 2D array(linked lists)
    for i in range(m):
        row = []
        for j in range(n): #iterates from 0-n creating the rows
            row.append('wall')
            #TO SEE HOW FOR LOOP WORKS UNCOMMENT AND CALL THE Function
            #print("i:" + str(i) +"and j:" + str(j))
            #print(row)
        grid.append(row)
    #print(grid)
    #creating random points to set 'start' to.
    start_i = randint(0, m - 1)
    start_j = randint(0, n - 1)
    grid[start_i][start_j] = 'start'
    #mowing the maze by creating empty cells using recursion
    mow(grid, start_i, start_j)
    #exploring the maze using using a BFS algorithms and dropping "candy" and finding the end of the of the
    explore_maze(grid, start_i, start_j, swag)
    return grid


#Recursively function which randomly picks a direction to explore from the 'start' point. It moves 2 places in that direction and then if that place is a "wall" it will set the cell to empty. Also the cell connecting start and the empty cell is also set to empty so a path is emerged.

def mow(grid, i, j):
    #i - COLUMN index
    #j - ROW index
    directions = ['U', 'D', 'L', 'R']
    while(len(directions) > 0):
        directions_index = randint(0, len(directions) - 1) #-1 is used because the length of the list is one extra than the index of the last element of the list
        direction = directions.pop(directions_index) #return and pop idx of direction

        #following code looks if we can move in any direction
        if direction == 'U': # when we travel UP the grid, our i(ROW) index decreases
            if i - 2 < 0: #if true we are ouside of bounds of our grid
                continue
            elif grid[i - 2][j] == 'wall': #sets to empty if theres walls in the up direction
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j) #recursively calling mow from  the place we just mowed

        elif direction == 'D':  #when we travel DOWN the grid, our i(ROW) index increases
            if i + 2 >= len(grid): #len looks at length of column
                continue
            elif grid[i + 2][j] == 'wall': # sets to empty if theres a wall
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j) #recursively calling mow from  the place we just mowed

        elif direction == 'L': #when we travel LEFT the grid, our j(COLUMN) index decreases
              if j - 2 < 0:
                continue
              elif grid[i][j-2] == 'wall':
                grid[i][j-1] = 'empty'
                grid[i][j-2] = 'empty'
                mow(grid, i, j - 2) #recursively calling mow from  the place we just mowed

        else: # going RIGHT
            if j + 2 >= len(grid[0]): #len looks at length of ROWS
                continue
            elif grid[i][j+2] == 'wall':
                grid[i][j+1] = 'empty'
                grid[i][j+2] = 'empty'
                mow(grid, i, j + 2) #recursively calling mow from  the place we just mowed
    return


def explore_maze(grid, start_i, start_j, swag):
    grid_copy = [row [:] for row in grid]
    bfs_queue = [ [start_i, start_j] ]
    directions = ['U', 'D', 'L', 'R']
    while len(bfs_queue) > 0:
        #pop dequeues and returns the pair of cooredinates
        current_i, current_j = bfs_queue.pop(0)
        # if we are not on start and between
        if grid[current_i][current_j] != 'start' and randint(1,10) == 1:
            grid[current_i][current_j] = swag[randint(0, len(swag) - 1)] #-1 is used because the length of the list is one extra than the index of the last element of the list
        grid_copy[current_i][current_j] = 'visited'
        for direction in directions:
            explore_i = current_i
            explore_j = current_j
            if direction == "U":
                explore_i = current_i - 1
            elif direction == "D":
                explore_i = current_i + 1
            elif direction == "L":
                explore_j = current_j - 1
            else: # direction R
                explore_j = current_j + 1

            #The below if statemenet looks if explore_i, explore_j are within the maze , and if they are not they are not appended to the que
            if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
                continue
            elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                bfs_queue.append([explore_i, explore_j])
    #value for current_i and current_j is the last furthest stop, set as end.
    grid[current_i][current_j] = 'E'


def print_maze(grid): # function takes care of formatting the maze
    for row in grid:
        printable_row = ''
        for cell in row:
            if cell == 'wall':
                char = '|'
            elif cell == 'start':
                char = 'X'
            elif cell == 'empty':
                char = ' '
            else:
                char = cell[0]

            printable_row += char
        print(printable_row)


print_maze(build_maze(20, 31, ['candy corn', 'werewolf', 'pumpkin']))
