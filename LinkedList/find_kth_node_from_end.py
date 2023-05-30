class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(ll, k_times):
    # Initialize both slow and fast pointers to head
    slow = fast = ll.head

    # Move the fast pointer k nodes ahead
    for _ in range(k_times):
        if fast is None:
            return None  # List is shorter than k
        fast = fast.next

    # Move slow and fast pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Return the slow pointer (k-th node from the end)
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2

result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
