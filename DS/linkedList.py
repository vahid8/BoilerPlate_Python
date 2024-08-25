class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create a node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        #create a node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Add the address to the current tail
            self.tail.next = new_node
            # update tail to current node
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value):
        # create a node
        new_node = Node(value)
        # add it to the begining
        temp = self.head  # save the current head
        self.head = new_node
        new_node.next = temp
        if self.length == 0:
            self.tail = new_node

        self.length += 1

    def insert(self, index, value):
        # create a node
        new_node = Node(value)
        # insert node
        wanted_node = self.head
        for i in range(index):
            wanted_node = wanted_node.next

        new_node.next = wanted_node.next
        wanted_node.next = new_node

        self.length += 1

    def pop(self):
        if self.length > 1:
            wanted_node = self.head
            for i in range(self.length-2):
                wanted_node = wanted_node.next

            wanted_node.next = None
            self.tail = wanted_node
            self.length -= 1

        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        else:
            return False




    def print_linkeList(self):
        if self.head is not None:
            temp = self.head
            for i in range(self.length):
                print(temp.value)
                temp = temp.next

if __name__ == '__main__':
    a = LinkedList(10)
    a.append(4)
    a.append(5)
    a.print_linkeList()
    a.pop()
    a.print_linkeList()

    a.pop()
    a.print_linkeList()
    print("--3--------")
    a.pop()
    a.print_linkeList()
    print("----------")
    a.append(45)
    a.print_linkeList()