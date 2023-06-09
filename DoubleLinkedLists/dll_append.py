class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
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

    def append(self, value):
        # new node to add
        new_node = Node(value)
        # edge case where there isn't any ddl
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # old tail next is now connected to node
            new_node.prev = self.tail  # reverse connection from new node  is connected to old tail
            self.tail = new_node  # now update to the new tail
        self.length += 1  # increase length of dll
        return True


if __name__ == "__main__":
    my_dll = DoubleLinkedList(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.print_list()
