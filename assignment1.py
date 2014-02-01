
colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#####################

p =[[0.05, 0.05, 0.05, 0.05, 0.05],
[0.05, 0.05, 0.05, 0.05, 0.05],
[0.05, 0.05, 0.05, 0.05, 0.05],
[0.05, 0.05, 0.05, 0.05, 0.05]]

def sense(p, Z):
    
    q =[[0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0]]
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])

            q[i][j] =(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))

    return q

def move(p, U):
    q =[[0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0]]


    for i in range(len(p)):
            for j in range(len(p[i])):
                q[i-U[0]][j-U[1]] += ((1-p_move)*p[(i-U[0]) % len(p)][(j-U[1]) % len(p[i])])
                q[i][j]+=(p_move*p[(i-U[0]) % len(p)][(j-U[1]) % len(p[i])])
    return q

for i in range(len(measurements)):
    p = move(p,motions[i])
    p = sense(p,measurements[i])

s=0
for i in range(len(p)):
    s+= sum(p[i])

    
for i in range(len(p)):
    for j in range(len(p[i])):
        p[i][j] = p[i][j] / s


############################


#Your probability array must be printed 
#with the following code.

show(p)
