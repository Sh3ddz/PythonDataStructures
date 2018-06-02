import DataStructures

linkedList = DataStructures.LinkedList()
linkedQueue = DataStructures.LinkedQueue()
linkedStack = DataStructures.LinkedStack()

node = DataStructures.Node(15)
node2 = DataStructures.Node("SIXTEEN")
node3 = DataStructures.Node(17)

print("------------------LINKED LIST TESTING------------------")
linkedList.add(node)
linkedList.add(node2)
linkedList.add(node3)
linkedList.add(DataStructures.Node(18))
print(linkedList)

print("AT INDEX 1:"+str(linkedList.get(1).getData()))

print("inserting at index 1")
linkedList.insert(DataStructures.Node(20),1)
print(linkedList)
print("AT INDEX 1:"+str(linkedList.get(1).getData()))

print("removing index 1")
linkedList.remove(1)
print(linkedList)
print("removing index 1")
linkedList.remove(1)
print(linkedList)

print("Clearing Linked List")
linkedList.clear()
print(linkedList)

print("------------------LINKED QUEUE TESTING------------------")
linkedQueue.add(node)
linkedQueue.add(node2)
linkedQueue.add(node3)
linkedQueue.add(DataStructures.Node(18))
print(linkedStack)

while(not linkedQueue.isEmpty()):
    print("Removing one element from the queue.")
    linkedQueue.remove()
    print(linkedQueue)

print("------------------LINKED STACK TESTING------------------")
linkedStack.add(node)
linkedStack.add(node2)
linkedStack.add(node3)
linkedStack.add(DataStructures.Node(18))
print(linkedStack)

while(not linkedStack.isEmpty()):
    print("Removing one element from the stack.")
    linkedStack.remove()
    print(linkedStack)