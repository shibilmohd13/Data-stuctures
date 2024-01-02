class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.end = True

    def search(self, word):
        node = self.root
        for char in word:   
            if char not in node.child:
                return False
            node = node.child[char]
        return node.end

    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False    
            node = node.child[char]
        return True


    def prefix_search(self, prefix):
        res = []
        node = self.root
        for char in prefix:
            if char not in node.child:
                return res
            node = node.child[char]
        self.prefix_helper(node, prefix, res)
        return res


    def prefix_helper(self, node, current_prefix, results):
        if node.end:
            results.append(current_prefix)
        for char, child in node.child.items():
            self.prefix_helper(child, current_prefix + char, results)

