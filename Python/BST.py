class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

class BST:
    
    def __init__(self, data):
        self.root = Node(data)
        
    def insert(self, data):
        self.root = self._insert(self.root, data)
        
    def _insert(self, node, data):
        if node is None:
            return Node(data)
            
        if data < node.key:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        
        return node
    
    def search(self, data):
        return self._search(self.root, data)
        
    def _search(self, node, data):
        
        if node is None:
            return False
            
        if node.key == data:
            return True
            
        if data < node.key:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
            
    def preorder(self):
        self._preorder(self.root)
        
    def _preorder(self, node):
        
        if node:
            print(node.key, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)
            
    def inorder(self):
        self._inorder(self.root)
        
    def _inorder(self, node):
        
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)
            
    def postorder(self):
        self._postorder(self.root)
        
    def _postorder(self, node):
        
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=" ")
        
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        
        if data < node.key:
            node.left = self._delete(node.left , data)
        elif data > node.key:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._get_min(node.right).key
            node.right = self._delete(node.right, node.key)

        return node
    
    def _get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current 

    def closest(self, target):
        return self.closest_value(self.root, target)

    def closest_value(self, node, target):
        closest = node.key
        while node:

            if abs(node.key - target) < abs(closest - target):
                closest = node.key

            if target < node.key:
                node = node.left
            elif target > node.key:
                node = node.right
            else:
                return node.key
        return closest

    def validate_bst(self, root):
        values = []

        def in_order_traversal(node):
            if node:
                in_order_traversal(node.left)
                values.append(node.key)  # Replace with the correct attribute
                in_order_traversal(node.right)

        in_order_traversal(root)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True




        