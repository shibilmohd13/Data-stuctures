class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with_prefix(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

# Example usage:
trie = Trie()
words = ["apple", "app", "apricot", "banana", "bat"]
for word in words:
    trie.insert(word)

search_word = "app"
print(f"Is '{search_word}' present in the trie? {trie.search(search_word)}")

prefix = "ap"
print(f"Does the trie have words with the prefix '{prefix}'? {trie.starts_with_prefix(prefix)}")
