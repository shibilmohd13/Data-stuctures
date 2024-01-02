# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

#     def insert(self, key):
#         if key < self.key:
#             if self.left is None:
#                 self.left = TreeNode(key)
#             else:
#                 self.left.insert(key)
#         elif key > self.key:
#             if self.right is None:
#                 self.right = TreeNode(key)
#             else:
#                 self.right.insert(key)

#     def contains(self, key):
#         if key == self.key:
#             return True
#         elif key < self.key and self.left:
#             return self.left.contains(key)
#         elif key > self.key and self.right:
#             return self.right.contains(key)
#         return False

#     def delete(self, key):
#         if key < self.key and self.left:
#             self.left = self.left.delete(key)
#         elif key > self.key and self.right:
#             self.right = self.right.delete(key)
#         else:
#             if self.left is None:
#                 return self.right
#             elif self.right is None:
#                 return self.left

#             min_key = self.right.find_min()
#             self.key = min_key
#             self.right = self.right.delete(min_key)

#         return self

#     def find_min(self):
#         current = self
#         while current.left:
#             current = current.left
#         return current.key

#     def inorder_traversal(self):
#         result = []
#         if self.left:
#             result.extend(self.left.inorder_traversal())
#         result.append(self.key)
#         if self.right:
#             result.extend(self.right.inorder_traversal())
#         return result

# # Example usage:
# bst = TreeNode(27)
# bst.insert(14)
# bst.insert(35)
# bst.insert(10)
# bst.insert(19)
# bst.insert(31)
# bst.insert(42)

# print("In-order traversal:", bst.inorder_traversal())

# # Search for a key
# search_key = 14
# print(f"Does the tree contain {search_key}? {bst.contains(search_key)}")

# # Delete a key
# bst = bst.delete(14)
# print("After deleting 14, in-order traversal:", bst.inorder_traversal())
