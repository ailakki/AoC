def full_(list):
    out =[]
    for c in range(len(list)):
        char = list[c]
        if len(out)==0:
            out.append(char)
        elif react(out[-1],char):
            out= out[:-1]
        else:
            out.append(char)
    return out

def react(c1,c2):
    if c1.islower() ==c2.islower() or c1.isupper() ==c2.isupper():
        return False
    elif c1.lower()==c2 or c1==c2.lower():
        return True
    else:
        return False

def remove_alfa(char,list):
    out= []
    for x in list:
        if x==char.lower() or x==char.upper():
             pass
        else:
             out.append(x)
    return out


if __name__ == "__main__":
    f= open("input.txt","r")
    line= []
    abc = 'abcdefghijklmnopqrstuvwxyz'
    min=0

    for l in f:
        line = [x for x in  l.strip()]

    for c in abc:
        output= full_(remove_alfa(c,line))
        if min > len(output) or min==0:
            min = len(output)
    print( min)
