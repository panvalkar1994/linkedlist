from LinkedList import create_list, Node, print_list

l1 = create_list(list('ABCDEFGH'))
print_list(l1)

def create_loop_in_list(head:Node, pos:int):
    cur = head

    while cur.next is not None:
        cur = cur.next
    
    n = head
    for i in range(pos):
        if n is None:
            raise Exception("Invalid position provided")
        n = n.next
    cur.next = n

    return head

loop = create_loop_in_list(l1, 2)

# print loop
# for i in range(20):
#     print(loop.data, end="->")
#     loop = loop.next
# print()

def detect_loop(head:Node):
    if head is None or head.next is None:
        return False
    fast = head.next.next
    slow = head
    while fast and slow:
        if fast == slow:
            return True
        if fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next
    return False
        
print(detect_loop(l1))