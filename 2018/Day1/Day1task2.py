import operator
ops = { "+": operator.add, "-": operator.sub }


def frequncyCalc(file):
    with open(file) as f:
        text = list(f)

        check_list = [0]
        search = True

        while True:
            if search:
                check_list,search= run(check_list,text)
            else:
                #print('break')
                break

        return check_list[-1]



def calc(total,line):
    op  = line[0]
    nr  = int(line[1:])
    return ops[op](total,nr)

def run(check_list,text):
    for line in text:
        tmp_out=calc(check_list[-1],line)
        if tmp_out in check_list:
            check_list.append(tmp_out)
            return check_list,False
        else:
            check_list.append(tmp_out)
    return check_list,True


print(frequncyCalc("input1.txt"))
