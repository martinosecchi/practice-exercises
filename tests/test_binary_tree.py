import unittest
from binary_tree import Node, max_depth, max_depth_simple

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        """
        Create a binary tree with this shape:
                   1
               2       3
            4  5       6   7
                               8
        """

        root = Node(1)
        
        # first level
        n2 = Node(2)
        n3 = Node(3)
        root.left = n2
        root.right = n3
        
        # second level
        n4 = Node(4)
        n5 = Node(5)
        n2.left = n4
        n2.right = n5

        n6 = Node(6) 
        n7 = Node(7)
        n3.left = n6
        n3.right = n7

        # extra leaf
        n8 = Node(8)
        n7.right = n8

        self.root = root

    def test_max_depth(self):
        assert max_depth(self.root) == 4

    def test_max_depth_simple(self):
        assert max_depth_simple(self.root) == 4

    def test_max_depth_methods_are_equivalent(self):
        assert max_depth(self.root) == max_depth_simple(self.root)



if __name__ == '__main__':
    unittest.main()
