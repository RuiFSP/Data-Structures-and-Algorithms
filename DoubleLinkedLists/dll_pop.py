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

    def pop(self):

        # edge case 1: empty dll
        if self.length == 0:
            return None

        # initialise temp node
        temp = self.tail  # save the tail node

        # edge case 2: only one node in dll
        if self.length == 1:
            self.head = None
            self.tail = None

        # all other cases
        else:
            self.tail = self.tail.prev  # update the tail to the new tail
            self.tail.next = None  # break connection to the new tail
            temp.prev = None  # break connection to the old tail

        # decrease length of dll
        self.length -= 1

        # return the value of the popped node
        return temp


if __name__ == "__main__":
    print("\n--- Initial DDL ---")

    my_dll = DoubleLinkedList(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.append(4)
    my_dll.print_list()

    print("\n-- After popping ----")

    print(f"Popped: {my_dll.pop().value}")
    my_dll.print_list()
