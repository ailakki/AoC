import re

def f1(file):
    f = open(file,"r")
    stats = []

    for line in f:
        stats.append(line.strip().split(' '))

    tmp= (sorted(stats))
    lines = [[e[3],int(e[1][3:5])] for e in tmp]

    return freq(lines)

def freq(l):
    tot = 0
    elf = []
    d = dict()
    tmp_start = 0
    id = 0
    for stat in l:
        if stat[0].startswith('#'):
            id = stat[0]
            if id not in d:
                d[id] = [[0]for m in range(60)]

        elif stat[0] =='asleep':
            tmp_start = stat[1]

        elif stat[0] =='up':
            for m in range(tmp_start,stat[1],1):
                d[id][m][0] +=1

    for x in d:
        tmp_tot  =(sum([d[x][i][0] for i in range(len(d[x]))]))
        if tmp_tot > tot:
            tot= tmp_tot
            elf =([int(x.strip('#')) , d[x].index(max(d[x]))] )

    return(elf[0]*elf[1])

print(f1("input.txt"))
