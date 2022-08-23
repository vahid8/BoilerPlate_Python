class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def __str__(self):
        temp = self.top
        return_string = ''
        while temp is not None:
            return_string += str(temp.value) + ', '
            temp = temp.next
        return return_string

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

if __name__ == '__main__':
    my_stack = Stack(7)
    my_stack.push(23)
    my_stack.push(3)
    my_stack.push(11)
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)
