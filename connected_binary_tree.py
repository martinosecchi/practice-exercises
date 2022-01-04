from binary_tree import Node
from queue import Queue


class ConnectedNode(Node):
    """A node of a tree with two children nodes and an extra connection to its next sibling on the same level.
        10--->None
        / \
       3-->5-->None
       / \   \   
      4-->1-->2-->None
    """
    def __init__(self, value, left=None, right=None, next_right=None):
        super().__init__(value, left, right)
        self.next_right = None


def connect_dfs(root: ConnectedNode):
    """Connect the nodes to their right side sibling using DFS.
    """
    levels = {}
    def dfs(node, level):
        if node is None:
            return
        if not levels.get(level):
            levels[level] = []
        levels[level].append(node)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    for level, nodes in levels.items():
        node = nodes[0]
        for nextnode in nodes[1:]:
            node.next_right = nextnode
            node = nextnode


def connect_bfs(root: ConnectedNode):
    """Connect the nodes to their right side sibling using BFS.
    """
    queue = Queue()
    depths = Queue()
    prev_node = None
    prev_depth = -1
    queue.put_nowait(root)
    depths.put_nowait(0)
    while not queue.empty():
        node = queue.get_nowait()
        depth = depths.get_nowait()
        # if on same level, chain
        if depth == prev_depth:
            prev_node.next_right = node
        # put children in queue for bfs
        for child in (node.left, node.right):
            if child is not None:
                queue.put_nowait(child)
                depths.put_nowait(depth + 1)
        # update previous
        prev_node = node
        prev_depth = depth


