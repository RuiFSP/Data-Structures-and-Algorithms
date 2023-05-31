class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):

        if not self.head:
            return None

        # Create two dummy nodes, less_head and greater_head, to serve as the heads of the two new linked lists for
        # nodes less than x and nodes greater than or equal to x, respectively
        less_head = Node(0)
        greater_head = Node(0)

        # Initialize two pointers, less and greater, to point to the dummy heads of the respective lists
        less = less_head
        greater = greater_head

        # Traverse the original linked list:
        # If the current node's value is less than x, append it to the less list by updating the next reference
        # of the less pointer and moving the less pointer to the newly appended node.
        # Otherwise, append it to the greater list using the same process
        current = self.head
        while current:
            if current.value < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next

        # Connect the tail of the less list to the head of the greater list by updating the next reference of the
        # tail node of less to point to the head node of greater
        less.next = greater_head.next

        # Set the next reference of the tail node of the greater list to None to mark the end of the partitioned list
        greater.next = None

        # Return the head node of the less list as the new head of the partitioned list
        self.head = less_head.next
        return self.head


ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list()  # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list()  # Output: 3 2 1 5 8 10

"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10

"""
