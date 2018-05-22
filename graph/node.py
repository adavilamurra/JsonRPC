class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0

    def show(self, level=0):
        print "%s%s val=%d:" % (level*"  ", self.name, self.val)
        for c in self.children: 
            c.show(level + 1)

    def removeDuplicates(self):
        newListChildren = []
        for child in self.children:
            if child not in newListChildren:
                newListChildren.append(child)
        self.children = newListChildren

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

