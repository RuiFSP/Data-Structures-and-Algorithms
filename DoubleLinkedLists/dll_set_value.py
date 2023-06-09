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

    def prepend(self, value):
        # new node to add
        new_node = Node(value)
        # edge case where there isn't any ddl
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # new node next is now connected to head
            self.head.prev = new_node  # reverse connection from head is connected to new node
            self.head = new_node  # now update to the new head
        self.length += 1  # increase length of dll
        return True

    def pop_first(self):

        # initialise temp node to return the popped node value
        temp = self.head  # save the head node

        # edge case 1: empty dll
        if self.length == 0:
            return None

        # edge case 2: only one node in dll
        if self.length == 1:
            self.head = None
            self.tail = None

        # all other cases
        else:
            self.head = self.head.next  # update the head to the new head
            self.head.prev = None  # break connection to the old head

        # decrease length of dll
        self.length -= 1

        # return the value of the popped node
        return temp

    def get(self, index):

        # edge case 1 - empty
        if self.length == 0:
            return None

        # edge case 2 - index out of bounds
        if index < 0 or index >= self.length:
            return None

        # all the other cases
        # look in  the first half of the list
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                # print(temp.value)
                temp = temp.next

        # look in the second half of the list
        else:
            temp = self.tail  # need to start from the tail
            for _ in range(self.length - 1, index, -1):
                # print(temp.value)
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        temp = self.get(index) # sets temp node to the node at the index
        if temp:
            temp.value = value
            return True
        return False


if __name__ == "__main__":
    my_dll = DoubleLinkedList(11)
    my_dll.append(5)
    my_dll.append(13)
    my_dll.append(7)
    my_dll.append(8)
    my_dll.append(9)
    print("\nInitial dll\n")
    my_dll.print_list()

    print(f"\n\t--> getting node from HEAD at index 1, using 1-half of loop \n")
    print(f"The value at index 1 is: {my_dll.get(1).value}\n")
    print(f"We changed value at index 1 ?: {my_dll.set_value(1, 65)}\n")
    print("\nModified dll\n")
    my_dll.print_list()

    print(f"\n\t--> getting node from TAIL at index 3, using 2-half of loop \n")
    print(f"The value at index 3 is: {my_dll.get(3).value}\n")
    print(f"We changed value at index 3 ?: {my_dll.set_value(3, 43)}\n")
    print("\nModified dll\n")
    my_dll.print_list()
