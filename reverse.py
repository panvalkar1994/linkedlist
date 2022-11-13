from LinkedList import Node, create_list, print_list

data = list('abcde')
root = create_list(data)
print_list(root)
print('-'*50)


# def reverse(root:Node)->Node:
#     prev = None
#     cur = root
#     while cur:
#         next = cur.next
#         cur.next = prev
#         prev = cur
#         cur = next
#     return prev


def reverse(root:Node):
    if root is None or root.next is None:
        return root
    cur = reverse(root.next)
    root.next.next = root
    root.next = None
    return cur
    
head = reverse(root)
print_list(head)


    
    