from LinkedList import print_list, create_list, Node, join_list

data = [3, 5, 8, 5, 10, 2, 1]

root = create_list(data)
print_list(root)
print('-'*50)


def partition(root:Node, key):
    small = []
    big = []
    while root:
        if root.data<key:
            small.append(root.data)
        else:
            big.append(root.data)
        root = root.next
    
    root =  create_list(small)
    big_list = create_list(big)
    root = join_list(root, big_list)
    return root

root = partition(root, 5)
print_list(root)