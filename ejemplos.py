# Array
array = [1, 2, 3, 4, 5]
print(array[3])  # 4

# Lista enlazada

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.display())

# Pila LIFO (Last In, First Out)
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())

# Colas (Queues) FIFO (First In, First Out)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def show(self):
        return self.queue


new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.dequeue()
print(new_queue.show())
new_queue.enqueue(4)
new_queue.dequeue()
print(new_queue.show())


# Tabla Hash

hash_table = {}

hash_table["config"] = {}
hash_table["config"]["database"] = {}
hash_table["config"]["database"]["host"] = "127.0.0.1"
hash_table["config"]["database"]["port"] = "5432"
hash_table["config"]["database"]["user"] = "postgres"
hash_table["config"]["database"]["pass"] = "postgres"
hash_table["config"]["database"]["dbname"] = "test"

print(hash_table)
print(hash_table["config"]["database"]["dbname"])


# Set
set_example = { 1, 2, 3, 4, 5, 6 }
set_example.add(6)
set_example.add(7)
set_example.add(2)
set_example.add(10)
set_example.add(6)
set_example.add(5)
print(set_example)