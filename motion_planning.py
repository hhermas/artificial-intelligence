# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


def search():
    grid1 = grid
    location_set = [[0,init[0],init[1]]] 
    grid1[init[0]][init[1]] = 1
    test = False
    i=0
    while test == False:

        for location in location_set:
            location_set.remove(location)
            possible_motion = motion(location, grid1)
            # print "&&&"

            for test_location in possible_motion:
                if test_location[1:3] == goal:
                    test = True
                    return test_location
                else:
                    test = False
                    location_set.append(test_location)
        # print location_set



def motion(location, grid):
    # print "***"
    # print location
    possible_motion = []

    for motion in delta:
        
        new_location = ["",""]
        new_location[0]=location[1]+motion[0]
        new_location[1]=location[2]+motion[1]
        # print new_location

        if (len(grid)-1) >= new_location[0]>=0 and (len(grid[0])-1)>=new_location[1]>=0:
            if grid[new_location[0]][new_location[1]] == 0:
                possible_motion.append([location[0]+1, new_location[0], new_location[1]])
                grid[new_location[0]][new_location[1]] = 1

    # print possible_motion
    # print "!!!"
    # print possible_motion
    return possible_motion

def test(location):
    if location == goal:
        return 'goal'
    else:
        return 'keep going'

