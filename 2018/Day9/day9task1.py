from itertools import cycle
# 459 players; last marble is worth 71320 points

def game_calc(players,max):
    tabled=[0]
    curr=1
    value=0
    player=[0 for x in range(players) ]

    for i in range(1,max+1,1):
        play =i%players
        step = curr +2
        size= len(tabled)
        if (i%23)==0:
            curr -= 7
            if curr<0:
                curr+=size
            #print('play',play,len(tabled),curr)
            player[play]+= (i+ tabled.pop(curr))# -9 from placment of 23div wich would be +2 from current index
        elif step == size:
            tabled.append(i)
            curr=len(tabled)
        elif step > size:
            curr = 1
            tabled.insert(curr,i)
        elif step < size:
            curr = curr + 2
            tabled.insert(curr,i)
    return player

print(max(game_calc(459,71320*100)))
