class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def find_similar_words(root, query, similarity_threshold):
    query_set = set(query)
    results = []

    def dfs(node, current_word):
        if node.is_end_of_word:
            word_set = set(current_word)
            similarity = jaccard_similarity(query_set, word_set)
            if similarity >= similarity_threshold:
                results.append((current_word, similarity))

        for char, child in node.children.items():
            dfs(child, current_word + char)

    for char in query:
        if char in root.children:
            dfs(root.children[char], char)

    return results

# Example usage:
root = TrieNode()
word_list = ["apple", "apples", "orange", "banana", "grape", "grapes", "shabil"]
for word in word_list:
    insert_word(root, word)

query_word = "shibil"
similarity_threshold = 0.7
similar_words = find_similar_words(root, query_word, similarity_threshold)
print(f"Words similar to '{query_word}': {similar_words}")
