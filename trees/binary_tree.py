# binary_tree.py

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left = n2
n1.right = n3
n2.left = n4

# current = n1
# while current:
#     print(current.data)
#     current = current.left


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left)
    print(current.data)
    inorder(current.right)


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left)
    preorder(current.right)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left)
    postorder(current.right)
    print(current.data)


def levelorder(root_node):
    visited_nodes = []
    queue = deque([root_node])
    while queue:
        current = queue.popleft()
        visited_nodes.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited_nodes


print("Inorder traversal")
inorder(n1)
print("#" * 100)
print("Preorder traversal")
preorder(n1)
print("#" * 100)
print("Postorder traversal")
postorder(n1)
print("#" * 100)
print("Levelorder traversal")
print(levelorder(n1))
