
from data_structures import Node, Queue, Stack

class Tnode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def breadth_first(self):
        """
        Perform a breadth-first traversal of the tree and return the values of all nodes.

        Returns:
            list: A list containing the values of all nodes in breadth-first order.
        """
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return output

    def pre_order(self):
        """
        Perform a pre-order traversal of the tree and return the values of all nodes.

        Returns:
            list: A list containing the values of all nodes in pre-order.
        """
        output = []

        def _walk(root):
            output.append(root.value)
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        """
        Perform an in-order traversal of the tree and return the values of all nodes.

        Returns:
            list: A list containing the values of all nodes in in-order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            output.append(root.value)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self):
        """
        Perform a post-order traversal of the tree and return the values of all nodes.

        Returns:
            list: A list containing the values of all nodes in post-order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)
            output.append(root.value)

        _walk(self.root)
        return output

class BinarySearchTree(Tree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        """
        Add a new node with the given value to the Binary Search Tree.

        Args:
            value: The value to be added to the tree.

        Returns:
            None
        """
        if not self.root:
            self.root = Tnode(value)
            return

        def _add_node(node, value):
            if value < node.value:
                if node.left:
                    _add_node(node.left, value)
                else:
                    node.left = Tnode(value)
            elif value > node.value:
                if node.right:
                    _add_node(node.right, value)
                else:
                    node.right = Tnode(value)

        _add_node(self.root, value)

    def contains(self, value):
        """
        Check if the Binary Search Tree contains a node with the given value.

        Args:
            value: The value to search for in the tree.

        Returns:
            bool: True if the value exists in the tree, False otherwise.
        """
        def _search(node, value):
            if not node:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)


    def get_max(self):
        """
        Returns the maximum value of the given tree
        """
        def __max(node):
            if node is None:
                return None  # Return None for empty nodes

            _max = node.value

            left_max = __max(node.left)
            if left_max is not None and left_max > _max:
                _max = left_max

            right_max = __max(node.right)
            if right_max is not None and right_max > _max:
                _max = right_max

            return _max

        return __max(self.root)


            
            
            

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(30)
    bst.add(20)
    bst.add(5)
    bst.add(15)
    bst.add(25)
    bst.add(0)
    bst.add(35)
    
    print("breadth")
    print(bst.breadth_first())
    print("pre_order")
    print(bst.pre_order())
    print("in_order")
    print(bst.in_order())
    print("post_order")
    print(bst.post_order())
    print("Contains 20:", bst.contains(20))
    print("Contains 40:", bst.contains(40))
    print(bst.get_max())