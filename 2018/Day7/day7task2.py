

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
    for point in list:
        left.add(point[1])
        if point[1] in graph:
            graph[point[1]].append(point[0])
        else:
            graph[point[1]]=[point[0]]
    for point in list:
        if point[0] not in left and point[0] not in starts:
            starts.append(point[0])
    starts.sort()
    return starts, graph

def nr(c):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count= 60 #0 for test
    for e in abc:
        count+=1
        if c == e:
            return count

if __name__ == '__main__':
    links =[]
    for lines in open('input.txt',"r"):
        line= lines.split()
        links.append([line[1],line[-3]])
    queue, graph = start_graph(links)

    #queue being list of letters without dependency
    time=0
    workers = ['free' for x in range(5)] #2 for test
    task_in_work=[]
    finished=False
    while not finished:

        # place task to freeworkers until out of freeworker or task in queue

        if 'free' in workers and len(queue)>0:
            for i in range(len(workers)):
                if workers[i]=='free' and len(queue)>0:
                    workers[i]=nr(queue[0])
                    task_in_work.append([i,queue[0]])
                    queue.remove(queue[0])

        # finish a task/free a worker

        if len(task_in_work)>0:
            step = min([x for x in workers if type(x) is int])
            for i in range(len(workers)):
                if type(workers[i]) is int:
                    workers[i] = workers[i]-step
                if workers[i]==0:
                    for x in task_in_work:
                        if x[0]==i:
                            graph=remove_from_dict(x[1],graph)
                        workers[i]='free'
            time+=step
        # move newly  indepentent to task queue
        for key in graph:
            if len(graph[key])==0:
                 queue.append(key)
        # and remove them from graph
        for e in queue:
            if e in graph:
                del graph[e]
        # no more task to start or to do
        if len(queue)==0 and all([x==workers[0] for x in workers]):
            finished=True

    print('Finish time', time)
