
'''
Build a diciconary of dependency , removing letters as processed

'''

def remove_from_dict(c,dict):
    for key in dict:
        if c in dict[key]:
            dict[key].remove(c)
    return dict


def start_graph(list):
    graph = {}
    left = set()
    starts =[]
    for l in list:
        left.add(l[1])
        if l[1] in graph:
            graph[l[1]].append(l[0])
        else:
            graph[l[1]]=[l[0]]
    for l in list:
        if l[0] not in left and l[0] not in starts:
            starts.append(l[0])
    starts.sort()
    return starts, graph


if __name__ == '__main__':
    f= open('input.txt',"r")

    links =[]
    for lines in f:
        line= lines.split()
        links.append([line[1],line[-3]])
    canditats, graph = start_graph(links)

    #canditats being list of letters without dependency
    start=canditats[0]
    path=[]
    while len(canditats)>0:

        graph=remove_from_dict(start,graph)
        path.append(start)
        canditats.remove(start)

        # get newly canditats letters
        for key in graph:
            if len(graph[key])==0:
                 canditats.append(key)

        # remove from diciconary the canditats letter keys
        for e in canditats:
            if e in graph:
                del graph[e]
        # pick next start
        if len(canditats)>0:
            canditats.sort()
            start= canditats[0]

    print('path',''.join(path))

a= [1,'fr',10]
print(min([x for x in a if type(x) is int ]))

b=['d', 'f']

if int in a:
    print('test',a)
