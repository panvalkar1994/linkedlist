from LinkedList import Node, print_list, create_list


def kthLast(root: Node, k: int):
    fast = root
    i = 0
    while i < k:
        if fast is None:
            raise Exception("Bad K value")
        fast = fast.next
        i += 1

    while fast:
        fast = fast.next
        root = root.next
    return root


data = [1, 2, 3, 4, 5, 6, 7]

root = create_list(data)
print_list(root)
print('-'*50)
k_last = 1

k_elem = kthLast(root, k_last)

print(f'for {k_last}th last data is {k_elem.data}')
