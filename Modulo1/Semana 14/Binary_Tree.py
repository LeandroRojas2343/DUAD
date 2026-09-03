class Node: 
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None 


# Binary Tree class 
class BinaryTree:
    def __init__(self, root_value):
        # create the root node of the tree 
        self.root = Node(root_value)

    # Method to insert a new value 
    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value): 
        if value < current_node.value: 
            if current_node.left is None:
                current_node.left = Node(value)
            else: 
                self._insert_recursive(current_node.left, value)
        else: 
            if current_node.right is None: 
                current_node.right = Node(value)
            else: 
                self._insert_recursive(current_node.right, value)

    # Method to print the whole tree 
    def print_tree(self): 
        print("Complete tree (in-order):")
        self._print_recursive(self.root)
        print()

    def _print_recursive(self, node): 
        if node is not None: 
            self._print_recursive(node.left) 
            print(node.value, end=' ')
            self._print_recursive(node.right)


# Example of use 
tree = BinaryTree(10)   # 10 is the root 
tree.insert(5)    
tree.insert(15)
tree.insert(11)
tree.insert(9)

tree.print_tree()