
def manhatan_dis(p,q):
    return abs(p[0]-q[0])+abs(p[1]-q[1])

def make_grid(points,max_x,max_y):
        grid = [['.' for x in range(max_x)]for y in range(max_y)]
        #from 1 not 0
        lables = [p for p in range(1,len(points)+1)]
        label_lookup ={}

        for nr, p in enumerate(points):
            label_lookup[str(p)]= lables[nr]

        for x in range(len(grid)):
                for y in range(len(grid[0])):
                    shortest = max_x*max_y
                    lable ='.'
                    for p in points:
                        distance= manhatan_dis((y,x),p)

                        if distance < shortest:
                            shortest = distance
                            lable = label_lookup[str(p)]
                        elif distance == shortest:
                            lable= '.'
                    grid[x][y] = lable

        return grid , lables


if __name__=="__main__":
    f= open("input.txt","r")
    points = []
    for line in f:
        y,x = line.split(',')
        points.append([int(y),int(x)])

    #make outer edge with buffer of 5
    max_y = max([p[0] for p in points])+5
    max_x = max([p[1] for p in points])+5


    grid,lables =make_grid(points,max_x,max_y)

    not_candidates = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if x == 0 or y == 0 or x == max_x or y == max_y:
                not_candidates.add(grid[x][y])

    not_candidates.remove('.')
    candidates = set(lables) - not_candidates

    winner = 0
    for candidate in candidates:
        count=0
        for y in grid:
            for x in y:
                if x == candidate:
                    count+=1
        if count > winner:
            winner= count

    print('Loner',winner)
