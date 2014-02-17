# -----------
# User Instructions:
# 
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]

init = [0, 2]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand[init[0]][init[1]] = 0
    j = 0
    
    motion = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    # motion[init[0]][init[1]] = 0

    while not found and open!=[]:
        open.sort()
        open.reverse()
        next = open.pop()
        x = next[1]
        y = next[2]
        g = next[0]

        if next == []:
            found = True
       
        # expand[next[1]][next[2]] = g
        # j+=1
        
        # if x == goal[0] and y == goal[1]:
        #     found = True
            # print next
        else:
            for i in range(len(delta)):
                expand[next[1]][next[2]] = g
                j+=1
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2, x2, y2])
                        # motion[x][y] = 
                        closed[x2][y2] = delta_name[i]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if expand[i][j]==-1:
                expand[i][j]=99
                            
    print expand
    return expand
    # return expand #Leave this line for grading purposes!

search()



