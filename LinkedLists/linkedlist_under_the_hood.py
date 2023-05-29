# we think of a linked list as a set of nested dictionaries
# each dictionary represents a node in the linked list
# each dictionary has two keys: 'value' and 'next'
# the value is the value stored in the node
# the next is a pointer to the next node in the list

head = {
    'value': 1,
    'next': {
        'value': 2,
        'next': {
            'value': 3,
            'next': {
                'value': 4,
                'next': None
            }
        }
    }
}

print(head['next']['next']['value']) # 3


# this will only run with a linked list, it is just to showcase the analogy
# print(my_linked_list.head.next.next.value) => 3
