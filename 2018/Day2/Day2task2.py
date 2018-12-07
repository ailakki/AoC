
def ID_checksum(file):
    f= open(file,"r")

    lines = [l.strip() for l in f]

    while len(lines)>1:
        l1=lines.pop()
        for l2 in lines:
            if one_diff(l1,l2) <=1:
                return match(l1, l2)

def one_diff(str1,str2):
    count =0
    for c1,c2 in zip(str1,str2):
        if c1!=c2:
            count+=1
    return count

def match(str1,str2):
    out = ''
    for c1,c2 in zip(str1,str2):
        if c1!=c2:
            out+=''
        else:
            out+=c1
    return out

if __name__ == '__main__':
    print(ID_checksum("input.txt"))
