class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def rebalance(self, node):
        if node is None:
            return None

        self.update_height(node)

        balance = self.balance(node)

        if balance > 1:  # Left heavy
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif balance < -1:  # Right heavy
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def avl_tree_insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)
        elif key < node.key:
            node.left = self.avl_tree_insert(node.left, key, value)
        else:
            node.right = self.avl_tree_insert(node.right, key, value)

        return self.rebalance(node)

    def avl_tree_search(self, node, key):
        if node is None:
            return False
        elif node.key == key:
            return True
        elif key < node.key:
            return self.avl_tree_search(node.left, key)
        else:
            return self.avl_tree_search(node.right, key)

    def avl_tree_delete(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            node.left = self.avl_tree_delete(node.left, key)
        elif key > node.key:
            node.right = self.avl_tree_delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.avl_tree_find_min(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self.avl_tree_delete(node.right, successor.key)
        return self.rebalance(node)

    def avl_tree_find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current