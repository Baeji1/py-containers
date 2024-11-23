from typing import List
import math


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:

    def __init__(self, values: List) -> None:
        if len(values) == 0:
            raise ValueError(
                "cannot instantiate empty binary tree, a root value is required"
            )

        self._tree: Node = self._build_tree(values)
        self.root = self._tree
        # build tree here
        self._nodes: int = len(values)
        self.height: int = int(math.log(self._nodes, 2)) + 1
        self._index: int = 0

    def _build_tree(self, values: List) -> Node:
        return Node(values[0])

    def __len__(self) -> int:
        return len(self._tree)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._nodes:
            self._index = 0
            raise StopIteration
        value = self._tree[self._index]
        self._index += 1
        return value

    def __str__(self) -> str:
        return f"root: {self.root}  size: {self._nodes}"


def main():
    test_values: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    tree = BinaryTree(test_values)
    print(len(tree))
    for node in tree:
        print(node)
    print("done")
    for node in tree:
        print(node)


if __name__ == "__main__":
    main()


"""
1. Arrays
2. Linked Lists
3. Stacks
4. Queues
5. Maps & Hash Tables
6. Graphs
7. Trees
8. Binary Trees & Binary Search Trees
9. Self-balancing Trees (AVL Trees, Red-Black Trees, Splay Trees)
10. Heaps
11. Tries
12. Segment Trees
13. Fenwick Trees
14. Disjoint Set Union
15. Minimum Spanning Trees
ropes
fibonacci trees
b trees

"""
