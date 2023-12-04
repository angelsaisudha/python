class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        postOrder(root.data,end =" ")
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.left.right = Node(6)
print("postorder Traversal:",end =" ")
postOrder(root)