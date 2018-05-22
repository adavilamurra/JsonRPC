import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
import sys

# Class providing functions for the client to use:
@service_class
class ServerServices(object):
    global tree
    tree = []
    
    @request
    #increment the value of every node of a graph
    def incrementProcess(self, root):
        self.tree = root
        self.increment(self, self.tree)
        return self.tree

    @request
    #convert the tree/graph made of lists to a JSON string and write it into a file
    def writeOnFile(self):
        with open("request.json", "w") as jsonFile:
            treeString = str(self.tree)
            treeString = treeString.replace("u", "")
            treeString = treeString.replace("[", "{")
            treeString = treeString.replace("]", "}")
            treeString = treeString.replace("'name',", "'name':")
            treeString = treeString.replace("'val',", "'val':")
            treeString = treeString.replace("'children',", "'children':")
            treeString = treeString.replace("'children': {{", "'children': [{")
            treeString = treeString.replace("{}", "[]")
            treeString = treeString[1:len(treeString)-1]
            treeString = treeString.replace("}}}", "}]}")
            jsonFile.write(treeString)
            jsonFile.close()
        return treeString

    @request
    def increment(self, root):
        for node in root:
            node[3] += 1
            print node
            if len(node[5]) != 0:
                self.increment(self, node[5])

def listen():
    # Quick-and-dirty TCP Server:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('localhost', 50001))
    serverSocket.listen(10)
    print "Server listening..."
    return serverSocket

def acceptConnection(serverSocket):
    while True:
        s, _ = serverSocket.accept()
        # JSONRpc object spawns internal thread to serve the connection.
        JSONRpc(s, ServerServices())
        sys.exit()

def startServer():
    serverSocket = listen()
    acceptConnection(serverSocket)

startServer()