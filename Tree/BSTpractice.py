class Node:
    def __init__(self, data) -> None:
        self.key = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        self.insert_node(self.root, data)

    def insert_node(self, node , data):
        if node.key is None:
            self.root = Node(data)
            return
        
        if data < node.key:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_node(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_node(node.right, data)
    
    def search(self, data):
        self.search_node(self.root, data)

    def search_node(self, node, data):
        if node is None:
            return False
        
        if node.key == data:
            return True
        
        if data < node.key:
            return self.search_node(node.left ,data)
        else:
            return self.search_node(node.right, data)

    def preorder(self):
        self.preorder_traversal(self.root)

    def preorder_traversal(self, node):
        if node:
            print(node.key , end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def inorder(self):
        self.inorder_traversal(self.root)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end = " ")
            self.inorder_traversal(node.right)      

    def postorder(self):
        self.postorder_traversal(self.root)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=" ")

    def delete(self, data):
        self.root = self._delete(self.root, data)
        return True  # Or return True/False based on deletion success

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.key:
            node.left = self._delete(node.left, data)
        elif data > node.key:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._find_min(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.key
