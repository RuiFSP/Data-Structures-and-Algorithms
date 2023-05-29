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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # need to append more nodes, but the focus is first to print the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


# starting a linked list with "ONE" node with value 23
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

# printing the head value of my linked list
my_linked_list.print_list()
