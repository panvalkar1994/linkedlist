from LinkedList import print_list, create_list, Node

data = list("abcdef")

root = create_list(data)
print_list(root)
print('-'*50)


def delete_middle_node(root:Node, key):
    if not root or not root.next:
        raise Exception('cannot delete first element')
    
    while root and root.next:
        if root.next.data==key:
            root.next = root.next.next
            return
        root = root.next
    
    
delete_middle_node(root, 'c')

print_list(root)