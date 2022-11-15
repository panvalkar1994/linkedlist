class Node:
    def __init__(self, data, next=None) -> None:
        self.data=data
        self.next=next

def append_node(root:Node, data):
    if root is None:
        root = Node(data)
        return root
    node = root
    while node.next is not None:
        node = node.next
    node.next=Node(data)
    return root

def print_list(root:Node):
    while root is not None:
        print(root.data, end="->")
        root = root.next
    print('\0')


def create_list(data:list):
    root = None
    for d in data:
        root = append_node(root, d)
    return root

def join_list(l1:Node, l2:Node):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    ptr = l1
    while ptr.next:
        ptr = ptr.next
    ptr.next = l2
    return l1