class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def __str__(self):
        temp = self.first
        return_string = ''
        while temp is not None:
            return_string += str(temp.value) + ', '
            temp = temp.next
        return return_string

    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1

        return temp.value


if __name__ == '__main__':
    task_queue = Queuer(4)
    task_queue.enqueue(6)
    task_queue.enqueue(8)
    task_queue.enqueue(10)
    task_queue.enqueue(12)
    print(task_queue)
    print("dequeue")
    print(task_queue.dequeue())
    print("after dequeue")
    print(task_queue)
