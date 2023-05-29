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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return  # some future method will require a boolean to be returned

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    def pop(self):
        # 1) case with node = 0
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        # 3) case with nodes >= 2
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre  # this will be the last node now
        self.tail.next = None  # update the new tail
        self.length -= 1  # update the new length

        # 2) case with node = 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value  # return the removed node, for testing will return the value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True  # some future method will require a boolean to be returned

    def pop_first(self):

        # edge case 1 - empty
        if self.length == 0:
            return None

        # all the other cases
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # edge case 2 - one element after decrement
        if self.length == 0:
            self.tail = None

        return temp.value  # for testing purpose

    def get(self, index):

        if index < 0 or index > self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp


if __name__ == "__main__":
    my_ll = LinkedList(0)
    my_ll.append(1)
    my_ll.append(2)
    my_ll.append(3)
    my_ll.print_list()

    print(f"\n--> appending a new node to start")
    print(my_ll.prepend(1))  # boolean confirming

    my_ll.print_list()

    print(f"\n--> popping node at start")
    print(my_ll.pop_first())  # what element was removed

    my_ll.print_list()

    print(f"\n--> getting nodes")
    print("\n")
    print(my_ll.get(-1))
    print(my_ll.get(0))
    print(my_ll.get(1))
    print(my_ll.get(2))
    print(my_ll.get(3))
    print(my_ll.get(4))
