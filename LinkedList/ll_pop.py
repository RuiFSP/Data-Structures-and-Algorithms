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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
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


if __name__ == "__main__":
    # example
    my_ll = LinkedList(1)
    my_ll.append(2)
    my_ll.print_list()
    print(f"\t We have now {my_ll.length} nodes in Linked List\n")
    # popping last element
    while my_ll.length > 0:
        print(f"Popping last element with value of {my_ll.pop()}")
        print(f"\t-->  {my_ll.length} nodes in Linked List\n")



