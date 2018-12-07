
def sum_s(str):
    abc= "abcdefghijklmnopqrstuvwxyz"
    twos = 0
    threes=0
    for l in abc :
        if str.count(l) ==3:
            threes=1
        elif str.count(l) ==2:
            twos=1

    return twos,threes


#print(ID_checksum("input.txt"))
if __name__=="__main__":
    f= open("input.txt","r")

    twos = []
    threes=[]

    for l in f:
        line =  l.rstrip()
        (tmp2,tmp3)=sum_s(line)
        twos.append(tmp2)
        threes.append(tmp3)
    print (sum(twos)*sum(threes))
