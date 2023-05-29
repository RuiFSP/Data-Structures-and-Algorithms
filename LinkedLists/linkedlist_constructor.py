# good practice to create a class for each node in linked list
# we are going to repeat ourself for everytime we need to append, prepend, insert
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node  # head is pointing to the first node created
        self.tail = new_node  # tail is pointing to the same value of head
        self.length = 1


# starting a linked list with "ONE" node with value 23
my_linked_list = LinkedList(23)

# printing the head value of my linked list
print(my_linked_list.head.value)
