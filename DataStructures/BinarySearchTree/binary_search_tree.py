from typing import List


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_tree_traversal(self) -> List:
        """returns items inserted into the tree in sorted order"""
        items = []

        self._recursive_tree_traversal(self.root, items)

        return items

    def _recursive_tree_traversal(self, node, items):
        """traversals the tree and appends values in sorted order"""
        if not node:
            return

        self._recursive_tree_traversal(node.left, items)
        items.append(node.val)
        self._recursive_tree_traversal(node.right, items)

    def search(self, val):
        """returns the first occurrence of a node with a given value """
        node = self.root
        while node and not node.val == val:
            if node.val < val:
                node = node.right
            else:
                node = node.left
        return node

    def minimum(self):
        """returns lowest value present in the tree"""
        node = self.root
        return self._tree_minimum(node).val

    @staticmethod
    def _tree_minimum(node):
        """finds a node with the lowest value present in the tree"""
        while node.left:
            node = node.left
        return node

    def maximum(self):
        """returns the largest value present in the tree"""
        node = self.root
        return self._tree_maximum(node).val

    @staticmethod
    def _tree_maximum(node):
        """finds a node with the largest value present in the tree"""
        while node.right:
            node = node.right
        return node

    def tree_successor(self, node):
        """returns node's successor"""
        if node.right:
            return self._tree_minimum(node.right)

        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = node.parent

        return parent

    def tree_predecessor(self, node):
        """returns node's predecessor"""
        if node.left:
            return self._tree_maximum(node.left)

        parent = node.parent
        while parent and node == parent.left:
            node = parent
            parent = node.parent

        return parent

    def insert(self, val):
        """inserts a value into the tree"""
        node = self.root

        if not node:
            self.root = Node(val)
            return

        parent = None
        while node:
            parent = node
            if node.val > val:
                node = node.left
            else:
                node = node.right

        inserted = Node(val, parent=parent)
        if parent.val > val:
            parent.left = inserted
        else:
            parent.right = inserted

    def delete(self, val):
        """removes the first occurrence of given value in the tree"""
        return self._delete_node(self.search(val))

    def _delete_node(self, node):
        """removes a node from the tree"""
        if not node.left:
            self._replace(node, node.right)
            return

        if not node.right:
            self._replace(node, node.left)
            return

        successor = self._tree_minimum(node.right)
        if successor.parent != node:
            self._replace(successor, successor.right)
            successor.right = node.right
            successor.right.parent = successor

        self._replace(node, successor)
        successor.left = node.left
        successor.left.parent = node

    def _replace(self, u, v):
        """replaces node in the tree with the given one"""
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v:
            v.parent = u.parent
