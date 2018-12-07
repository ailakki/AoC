
def full_reaction(input):
    f= open(input,"r")
    out = []

    for l in f:
        line = l.strip()
        for char in line:
            if len(out)==0:
                out.append(char)
            elif react(out[-1],char):
                out= out[:-1]
            else:
                out.append(char)
    return len(out)

def react(c1,c2):
    if c1.islower() ==c2.islower() or c1.isupper() ==c2.isupper():
        return False
    elif c1.lower()==c2 or c1==c2.lower():
        return True
    else:
        return False

print(full_reaction("input.txt"))
