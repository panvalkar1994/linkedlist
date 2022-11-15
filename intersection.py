from LinkedList import Node, append_node, create_list, join_list, print_list

list_a = create_list(list("abcdefgh"))
list_b = create_list(list("ABCD"))
list_c = create_list(list("123"))

l1 = join_list(list_a, list_c)
l2 = join_list(list_b, list_c)

print('first list')
print_list(l1)
print('-'*50)


print('second list')
print_list(l2)
print('-'*50)

def find_intersection(head1:Node, head2:Node):
    p1 = head1
    p2 = head2

    while p1 or p2:
        if p1 is None:
            p1 = head2
        
        if p2 is None:
            p2 = head1

        if p1 == p2:
            return p1
        p1 = p1.next
        p2 = p2.next

    return p1

node = find_intersection(l1, l2)
print(node.data)