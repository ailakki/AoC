
class Node:
    def __init__(self, args):
        self.nr_childeren = args[0]
        self.metadata_points = args[1]
        self.metadata =[]
        self.childeren =[]
        self.parent= None
        self.value=0

    def get_nr_childeren(self):
        return self.nr_childeren 

    def set_value(self, a_value):
        self.value += a_value

    def get_value(self):
        return self.value

    def set_parent(self,node):
        self.parent=node

    def get_parent(self):
        return self.parent

    def add_data(self,data):
        #ints of metadata length = metadata_points
        self.metadata.append(data)
    def get_metadata(self):
        return self.metadata

    def add_child(self, node):
        # child nodes
        self.childeren.append(node)

    def get_childeren(self):
        return self.childeren

    def full_data(self):
        if len(self.metadata)==self.metadata_points:
            return True
        return False

    def full_child(self):
        if len(self.childeren)==self.nr_childeren:
            return True
        return False



def readin(text):
    info=[]
    for line in open(text,'r'):
        nrs =line.strip().split()
        info=[int(x) for x in nrs]
    return info

def build_tree(root,list):
    a_node=root
    args=list
    count=0
    while not root.full_data():
        #print(a_node.name)

        if a_node.full_child() and not a_node.full_data():

            count+=args[0]
            if a_node.get_nr_childeren() ==0:
                a_node.set_value(args[0])
                a_node.add_data(args.pop(0))
            else:
                a_node.add_data(args.pop(0))

            #a_node.add_data(args.pop(0))

        elif a_node.full_child() and a_node.full_data():
            a_node =a_node.get_parent()
            #args=args[2:]
        else:
            new_node = Node(args[0:2])
            new_node.set_parent(a_node)
            a_node.add_child(new_node)
            a_node=new_node
            args=args[2:]


def  find_value(node):
    if node.get_value()!=0:
        return node.get_value()
    else:
        for i in node.get_metadata():
            if i <= len(node.get_childeren()):
                node.set_value(find_value(node.get_childeren()[i-1]))
            else:
                node.set_value(0)
        return node.get_value()


if __name__ == '__main__':
    data=readin('input.txt')
    root=Node(data[0:2])
    list=data[2:]
    build_tree(root,list)
    print(find_value(root))
