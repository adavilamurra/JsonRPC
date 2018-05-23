# JSON Client-Server
Last modification date: 4/22/18

## How to run the program:
### Server
    "python jserver.py"
    
### Client
    "python jclient.py"
    
### Additional notes on how to run program:
    This program does not take in any parameters. First run the server, then the client.
    The only way to start the client and server is by running the commands above.

## Program Description:
    This program sends an object from a client to the server.
    The server sends it back and the client prints it.
    The object that is being sent is a simple graph. The nodes are made up a name, a value, and a list of children nodes. 
    The client will check that the graph's children are not repeated to avoid future errors or complications.
    This graph/object is converted into a combination of lists and then it is sent to the server.
    The server receives this node converted into a list and increases the value of each node.
    After that increment, the server send the incremented list to the client.
    Once the list is in the client, it will be converted into an object again (node) and then it will be printed.
    The client will also ask the server to create a JSON file with the JSON string for the graph with increased value in nodes.

## Author

* **Alejandro Davila** - [adavilamurra](https://github.com/adavilamurra)