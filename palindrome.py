from LinkedList import create_list, Node, print_list


data = list("abcddcbae")
root = create_list(data)
print_list(root)


def check_palindrome(root:Node):
    def fill_stack(root:Node):
        stack = []
        while root:
            stack.append(root.data)
            root = root.next
        return stack
    
    stack = fill_stack(root)
    while root:
        if root.data != stack.pop():
            return False
        root = root.next

    return True

print('check', check_palindrome(root))