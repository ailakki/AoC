import operator
ops = { "+": operator.add, "-": operator.sub }


def frequncyCalc(file):
    with open(file) as f:
        text = list(f)
        check_list = [0]
        run(check_list,text)

        return check_list[-1]



def calc(total,line):
    op  = line[0]
    nr  = int(line[1:])
    return ops[op](total,nr)

def run(check_list,text):
    for line in text:
        tmp_out=calc(check_list[-1],line)
        check_list.append(tmp_out)
    return check_list


print(frequncyCalc("input1.txt"))
