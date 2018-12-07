import numpy as np
import re


def overlap(file):
    f= open(file,"r")

    count = 0
    ufabric = [[] for x in range(1000)]
    overlap = [[] for x in range(1000)]
    ids=[]
    stats=[]

    for line in f:
        stats.append([int(nr)  for nr in  re.findall(r'-?\d+\.?\d*', line)])

    for stat in stats:
        id,px,py,xs,ys =stat

        for y in range(py,ys+py,1):
            for x in range(px,xs+px,1):
                if x in overlap[y]:
                    pass
                elif x in ufabric[y]:
                    count+=1
                    overlap[y].append(x)
                else:
                    ufabric[y].append(x)

    for stat in stats:
        id,px,py,xs,ys =stat
        ids.append(id)

        for y in range(py,ys+py,1):
            for x in range(px,xs+px,1):
                if x in overlap[y] and id in ids:
                    ids.remove(id)

    return count,ids
print(overlap("input.txt"))
