from connected_binary_tree import ConnectedNode, connect_bfs, connect_dfs
import unittest


def extract_next_rights(root: ConnectedNode) -> list:
    current = root
    levels = []
    while current is not None:
        current_level = []
        x = current
        while x is not None:
            current_level.append(x.value)
            x = x.next_right
        levels.append(current_level)
        current = current.left
    
    return levels


class TestConnectedBinaryTree(unittest.TestCase):
    
    def setUp(self):
        root = ConnectedNode(10)
        root.left = ConnectedNode(3)
        root.right = ConnectedNode(5)
        root.left.left = ConnectedNode(4)
        root.left.right = ConnectedNode(1)
        root.right.right = ConnectedNode(2)
        self.root = root

    def test_connect_dfs(self):
        connect_dfs(self.root)
        assert extract_next_rights(self.root) == [
            [10],
            [3, 5],
            [4, 1, 2],
        ]

    def test_connect_bfs(self):
        connect_bfs(self.root)
        assert extract_next_rights(self.root) == [
            [10],
            [3, 5],
            [4, 1, 2],
        ]


if __name__ == '__main__':
    unittest.main()