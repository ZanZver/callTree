class Node:
    def __init__(self, value, children=None):
        # a leaf node has an empty list of children
        if children is None:
            children = []
        self.value = value
        self.children = children

root = Node(1, [
    Node(2, [
        Node(3, [
            Node(4),
            Node(5)
        ]),
        Node(6)
    ]),
    Node(7, [
        Node(8, [
            Node(9)
        ])
    ]),
    Node(10)
])

def tree_sum(node):
    t = node.value
    for child in node.children:
        t += tree_sum(child)
    return t