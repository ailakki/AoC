
def manhatan_dis(p,q):
    return abs(p[0]-q[0])+abs(p[1]-q[1])

def make_grid(points,max_x,max_y):
        grid = [['.' for x in range(max_x)]for y in range(max_y)]

        for x in range(len(grid)):
                for y in range(len(grid[0])):
                    shortest = 10000
                    lable ='.'
                    distance = 0
                    for p in points:
                        distance += manhatan_dis((y,x),p)
                    if distance < shortest:
                        lable = '#'
                    elif distance == shortest:
                        lable= '.'
                    grid[x][y] = lable

        return grid


if __name__=="__main__":
    f= open("input.txt","r")
    points = []
    for line in f:
        y,x = line.split(',')
        points.append([int(y),int(x)])

    #make outer edge with buffer of 5
    max_y = max([p[0] for p in points])+5
    max_x = max([p[1] for p in points])+5

    grid =make_grid(points,max_x,max_y)

    winner = 0
    for y in grid:
        for x in y:
            if x == '#':
                winner+=1

    print('Area poits within ',winner)
