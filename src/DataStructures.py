# Node - holds data and a link to another node
class Node:
    def __init__(self, *args):
        if (args.__len__() == 0):
            self.data = None
            self.link = None
        if (args.__len__() == 1):
            self.data = args[0]
            self.link = None
        if (args.__len__() == 2):
            self.data = args[0]
            self.link = args[1]

    def getData(self):
        return self.data

    def getLink(self):
        return self.link

    def setData(self, data):
        self.data = data

    def setLink(self, link):
        self.link = link

    def __str__(self):
        return "[Data: " + str(self.data) + "]"


# LinkedList - List of connected Nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Returns if the LinkedList is empty or not
    def isEmpty(self):
        return self.head == None

    # Returns the Node stored at value index
    def get(self, index):
        nodeToGet = self.head
        for x in range(index):
            nodeToGet = nodeToGet.getLink()
        return nodeToGet

    # Adds element to the beginning of the LinkedList
    def addFirst(self, element):
        self.head = Node(element, self.head)

    # Adds element to the end of the LinkedList
    def add(self, element):
        if (self.head == None):
            self.addFirst(element)
        else:
            tmp = self.head
            while (tmp.getLink() != None):
                tmp = tmp.getLink()
            newNode = Node(element, None)
            tmp.setLink(newNode)

    # Inserts element at the specified index of the LinkedList
    def insert(self, element, index):
        if(index<0 or index>self.size()):
            print("Index out of bounds")
            return

        if(index == 0):
            self.addFirst(element)
        else:
            tmp = self.head
            oldLink = tmp.getLink()
            for x in range(index-1):
                tmp = oldLink
                oldLink = tmp.getLink()
            tmp.setLink(Node(element, oldLink))

    # Removes element at the specified index of the LinkedList
    def remove(self, index):
        if(index<0 or index>self.size()-1):
            print("Index out of bounds")
            return

        if(index == 0):
            self.head = self.head.getLink()
        else:
            nodeToConnectNext = self.head
            for x in range(index-1):
                nodeToConnectNext = nodeToConnectNext.getLink()

            nodeToConnectNext.setLink(nodeToConnectNext.getLink().getLink())

    # Returns the size of the LinkedList
    def size(self):
        if (self.head == None):
            return 0

        size = 1
        n = self.head
        while (n.getLink() != None):
            size += 1
            n = n.getLink()

        return size

    # Clears the LinkedList, makes it contain nothing.
    def clear(self):
        self.__init__()

    # Returns the string of the LinkedList
    def __str__(self):
        if(self.head == None):
            return "[EMPTY]"
        s = "["
        iter = 1
        n = self.head
        while (n.getLink() != None):
            if (iter < self.size()):
                s += str(n.getData()) + ", "
            else:
                s += str(n.getData())

            n = n.getLink()
            iter += 1

        s += str(n.getData()) + "]"
        return s


# LinkedQueue - First in first out
class LinkedQueue:
    def __init__(self):
        self.list = LinkedList()

    def isEmpty(self):
        return self.list.isEmpty()

    def add(self, element):
        self.list.add(element)

    def remove(self):
        self.list.head = self.list.head.getLink()

    def __str__(self):
        return "Queue: " + self.list.__str__()


# LinkedStack - First in Last out
class LinkedStack:
    def __init__(self):
        self.list = LinkedList()

    def isEmpty(self):
        return self.list.isEmpty()

    def add(self, element):
        self.list.add(element)

    def remove(self):
        self.list.remove(self.list.size()-1)

    def __str__(self):
        return "Stack: " + self.list.__str__()
