from LinkedList import print_list, Node, append_node

# node_data = [1,1,2,3,4,1,2,1,5,1]
node_data = []
root = None
for data in node_data:
    root = append_node(root, data)

print_list(root)

def removeDup(root:Node):
    """two pointers"""
    if root is None:
        return root
    slow = root
    while slow is not None:
        prev = root
        fast = slow.next
        while fast:
            if slow.data!=fast.data:
                prev=fast
            else:
                prev.next=fast.next
            fast=fast.next
        slow = slow.next

    return root

def removeDuplicate(root:Node):
    if not root:
        return
    s = set()
    s.add(root.data)
    while root.next:
        if root.next.data in s:
            root.next = root.next.next
        else:
            s.add(root.next.data)
            root = root.next
        
removeDuplicate(root)
print_list(root)


