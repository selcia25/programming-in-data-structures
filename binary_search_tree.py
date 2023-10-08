class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements = elements + self.right.inorder_traversal()
        return elements

    def preorder_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements = elements + self.left.preorder_traversal()
        if self.right:
            elements = elements + self.right.preorder_traversal()
        return elements

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.postorder_traversal()
        if self.right:
            elements = elements + self.right.postorder_traversal()
        elements.append(self.data)
        return elements

    def search(self, data):
        if self.data == data:
            return ("Found")
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return ("Not Found")
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return ("Not Found")

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max = self.left.find_max()
            self.data = max
            self.left = self.left.delete(max)

        return self

def build_tree(elements):
    root = TreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    elements = [54,21,2,1,22,74,58]
    numbers = build_tree(elements)
    print("Original input: ",elements)
    print("Inorder traversal: ",numbers.inorder_traversal())
    print("Postorder traversal: ",numbers.postorder_traversal())
    print("Preorder traversal: ",numbers.preorder_traversal())
    print("Maximum: ",numbers.find_max())
    print("Minimum: ",numbers.find_min())
    print("15 is",numbers.search(15),"in the tree")
    print("151 is",numbers.search(151),"in the tree")
    numbers.delete(2)
    print("Delete 2: ",numbers.inorder_traversal())
    numbers.delete(74)
    print("Delete 74: ",numbers.inorder_traversal())