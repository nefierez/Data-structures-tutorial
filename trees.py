class MyTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MyTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return MyTreeNode(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)
        return root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self._search(root.left, value)
        return self._search(root.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._minValueNode(root.right)
            root.value = temp.value
            root.right = self._delete(root.right, temp.value)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def forwardTraversal(self):
        self._forwardTraversal(self.root)

    def _forwardTraversal(self, root):
        if root:
            self._forwardTraversal(root.left)
            print(root.value, end=" ")
            self._forwardTraversal(root.right)

    def backwardTraversal(self):
        self._backwardTraversal(self.root)

    def _backwardTraversal(self, root):
        if root:
            self._backwardTraversal(root.right)
            print(root.value, end=" ")
            self._backwardTraversal(root.left)


# Test Scenario 1: Create the binary search tree
my_tree = MyTree()

# Test Scenario 2: Insert values one by one into the BST
my_tree.insert(4)
my_tree.insert(2)
my_tree.insert(6)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(5)
my_tree.insert(7)

# Test Scenario 3: Search for a value in the BST
search_value = 5

result = my_tree.search(search_value)
if result:
    print("Found", search_value, "in the BST.")
else:
    print(search_value, "not found in the BST.")

# Test Scenario 4: Delete a value from the BST
delete_value = 3
my_tree.delete(delete_value)
print(delete_value, "has been deleted from the BST.")

# Test Scenario 5: Perform forward traversal to print the BST elements in ascending order
print("Forward Traversal:")
my_tree.forwardTraversal()

# Test Scenario 6: Perform backward traversal to print the BST elements in descending order
print("\nBackward Traversal:")
my_tree.backwardTraversal()
