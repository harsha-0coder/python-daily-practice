# WRITE A PROGRAM TO IMPLEMENT SIMPLE BINARY TREE.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Traversal functions
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("This Code is written by Harsh ChOurasia\n")

# Print traversals
print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)
