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
        # Initialize and empty set to store unique value
        unique_set = set()

        # Initialize two pointers, previous and current
        previous = None
        current = self.head

        # Iterate through the list
        while current is not None:
            # if current node's value is already in the set, remove duplicate
            if current.value in unique_set:
                previous.next = current.next
                # decrement list length by 1
                self.length -= 1
            # Else, add the current node's value to the set and update previous
            else:
                unique_set.add(current.value)
                previous = current
            current = current.next


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
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
