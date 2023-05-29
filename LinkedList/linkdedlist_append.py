class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create new node
        new_node = Node(value)
        # in case there is not a node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # add node to tail
            self.tail = new_node # update tail
        self.length += 1
        return True  # it will be need later to check something, but is not needed for now

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)

my_ll.print_list()
