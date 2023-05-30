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
        return True  # some future method will require a boolean to be returned

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

    def set_value(self, index, value):
        # validate/search for index
        temp = self.get(index)

        if temp:  # validate input is true
            # update value
            temp.value = value
            return True
        return False

    def insert(self, index, value):

        # needs valid index
        if index < 0 or index > self.length:
            return False

        # reuse code if insert at start
        if index == 0:
            return self.prepend(value)

        # reuse code if insert at the end
        if index == self.length:
            return self.append(value)

        # the other conditions
        new_node = Node(value)  # node to add with value
        temp = self.get(index - 1)  # we end the previous node before we reach the desired index

        new_node.next = temp.next  # new node is pointing to next node from previous conditions
        temp.next = new_node  # previous node is pointing to the enw node
        self.length += 1  # increment length

        return True

    def remove(self, index):

        # case1 - check for valid index
        if index < 0 or index >= self.length:
            return None

        # case2 - remove from head
        if index == 0:
            self.pop_first()

        # case3 - remove from tail
        if index == self.length - 1:
            self.pop()

        # case4 - all the other cases
        prev = self.get(index - 1)
        temp = prev.next  # more efficient than self.get(index) O(1) > O(n)

        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp  # node removed

    def reverse(self):

        # reverse head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # new variables to help iterate the linked list
        # after = temp.next (not needed here, just to visualize
        before = None

        # iterate (before - temp - after)
        for _ in range(self.length):
            after = temp.next
            temp.next = before  # flips arrow
            before = temp  # move before for next iteration
            temp = after  # move temp for next iteration


if __name__ == "__main__":
    my_ll = LinkedList(0)
    my_ll.append(1)
    my_ll.append(2)
    my_ll.append(3)
    print("\n---My Initial List---")
    my_ll.print_list()
    print("\n")
    print(f"\n--> appending a new node to start")
    print(my_ll.prepend(1))  # boolean confirming

    my_ll.print_list()
    print("\n")

    print(f"\n--> popping node at start")
    print(my_ll.pop_first())  # what element was removed
    my_ll.print_list()
    print("\n")
    print(f"\n--> getting nodes")
    print(my_ll.get(-1))
    print(f"\t getting node 0 -> the value is: {my_ll.get(0).value}")
    print(f"\t getting node 1 -> the value is: {my_ll.get(1).value}")
    print(f"\t getting node 2 -> the value is: {my_ll.get(2).value}")
    print(f"\t getting node 3 -> the value is: {my_ll.get(3).value}")
    print(my_ll.get(4))

    print(f"\n--> updating value at index 2 for 32")
    my_ll.print_list()
    print(my_ll.set_value(2, 32))

    my_ll.print_list()
    print("\n")

    print(f"\n--> inserting node at index 1 for 11")
    print(my_ll.insert(1, 11))
    my_ll.print_list()
    print("\n")

    print(f"\n--> removing node at index 2")
    print(my_ll.remove(2))
    my_ll.print_list()
    print("\n")

    print(f"\n--> reversing linked list")
    print(my_ll.reverse())
    my_ll.print_list()
