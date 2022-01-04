from utils import compare


class Node:
    """A node class for binary trees.
    It has a value and a left and right children nodes.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node {}".format(self.value)

    def is_leaf(self):
        return self.left is None and self.right is None


def is_leaf(node: Node) -> bool:
    """Returns True if the node is a leaf node.
    """
    return node and node.is_leaf()


def max_depth(root: Node) -> int:
    """Finds the maximum depth of a binary tree.
    """
    def _depth(node, depth):
        if node is None:
            return depth
        return max(_depth(node.left, depth + 1), _depth(node.right, depth + 1))

    return _depth(root, 0)


def max_depth_simple(root: Node) -> int:
    """An alternative version of max_depth.
    """
    if root is None:
        return 0
    return 1 + max(max_depth_simple(root.left), max_depth_simple(root.right))


def is_bst(root: Node) -> bool:
    """
    Given a binary tree, return true if it is BST, else false. 
    For example, the following tree is not BST, because 11 is in left subtree of 10.

                10
        7               39
            11
    """
    def dfs(node: Node, value: int, expected_comparison: int):
        if node is None:
            return True
        elif compare(node.value, value) != expected_comparison:
            return False
        else:
            return dfs(node.left, value, expected_comparison) and dfs(node.right, value, expected_comparison)
        
    if root is None:
        return True
    elif not dfs(root.left, root.value, -1):
        return False
    elif not dfs(root.right, root.value, 1):
        return False
    
    return is_bst(root.left) and is_bst(root.right)

