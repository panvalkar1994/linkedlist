from LinkedList import create_list, Node, print_list, append_node

d1 = [7,1,6, 1] #1617
d2 = [5,9,4] #395

l1 = create_list(d1)
l2 = create_list(d2)

print('l1')
print_list(l1)
print('-'*50)

print('l2')
print_list(l2)
print('-'*50)

# def list_to_digit(root:Node):
#     val = 0
#     place = 1
#     while root:
#         val = (root.data*place) + val
#         place *= 10
#         root = root.next
#     return val

# l1_val = list_to_digit(l1)
# l2_val = list_to_digit(l2)

# val = l1_val + l2_val

# data = [int(d) for d in str(val)]
# data.reverse()
# root = create_list(data)
# print_list(root)

def sum_list(l1:Node, l2:Node):
    sum = 0
    carry = 0
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    root = None
    while l1 or l2:
        sum = 0
        if l1:
            sum += l1.data
            l1 = l1.next
        
        if l2:
            sum += l2.data
            l2 = l2.next
        
        sum += carry
        carry = sum//10
        sum = sum%10
        root = append_node(root, sum)
    
    if carry:
        root = append_node(root, carry)
    return root

root = sum_list(l1, l2)
print_list(root)