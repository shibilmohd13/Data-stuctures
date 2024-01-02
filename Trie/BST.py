class Node:
    def __init__(self, data) -> None:
        self.key = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data) -> None:
        self.root = Node(data)

    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.key:
            node.left = self._insert(node.left, data)
        
        else:
            node.right = self._insert(node.right , data)

        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        
        if node.key == data:
            return True
        elif data < node.key :
            return self._search(node.left , data)
        else:
            return self._search(node.right, data)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, res):
        if node:
            res.append(node.key)
            self._preorder(node.left, res)
            self._preorder(node.right, res)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(node.key)
            self._inorder(node.right, res)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, res):
        if node:
            self._postorder(node.left, res)
            self._postorder(node.right, res)
            res.append(node.key)


    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node

        if data < node.key:
            node.left = self._delete(node.left, data)
        
        elif data > node.key:
            node.right = self._delete(node.right, data)

        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            node.key = self.get_min(node.right).key
            node.right = self._delete(node.right , node.key)

        return node

    def get_min(self, node):
        current = node
        while current.left:
            current = current.left 
        return current

    def closest(self, node, target):
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
    
    def is_bst(self, node):
        values = []

        self._inorder(node, values)

        for i in range(1,len(values)):
            if values[i] <= values[i-1]:
                return False
        return True


        


        
            



        
