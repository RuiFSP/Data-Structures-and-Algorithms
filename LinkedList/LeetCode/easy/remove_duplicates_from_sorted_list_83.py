class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove_duplicates(self):
        current = self.head
        while current:
            while current.next and current.next.value == current.value:
                current.next = current.next.next
            current = current.next

        return self.head

my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(4)

print("\nOriginal List list\n")

my_linked_list.print_list()

print("\nRemoving duplicated items in sorted list\n")

my_linked_list.remove_duplicates()

my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4

"""
