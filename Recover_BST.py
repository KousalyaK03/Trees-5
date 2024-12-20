# Approach:
# A BST's in-order traversal gives nodes in sorted order. If two nodes are swapped, the order will be violated.
# 1. Perform an in-order traversal to identify the two swapped nodes.
# 2. During traversal, compare each node with the previous node.
# 3. The first swapped node is found when a node is smaller than its predecessor.
# 4. The second swapped node is found later when another smaller node is encountered.
# 5. Swap the values of the two identified nodes to restore the BST.

# Time Complexity: O(n), where n is the number of nodes, as we perform an in-order traversal.
# Space Complexity: O(1) (excluding recursion stack), as the solution uses constant space.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize pointers
        self.first = None  # First swapped node
        self.second = None  # Second swapped node
        self.prev = TreeNode(float('-inf'))  # Previous node in in-order traversal
        
        def in_order_traversal(node):
            # Base case
            if not node:
                return
            
            # Traverse the left subtree
            in_order_traversal(node.left)
            
            # Check for swapped nodes
            if not self.first and self.prev.val > node.val:
                self.first = self.prev  # First time the order is violated
            if self.first and self.prev.val > node.val:
                self.second = node  # Second time the order is violated
            
            # Update the previous node
            self.prev = node
            
            # Traverse the right subtree
            in_order_traversal(node.right)
        
        # Perform in-order traversal to find swapped nodes
        in_order_traversal(root)
        
        # Swap the values of the two nodes to fix the BST
        self.first.val, self.second.val = self.second.val, self.first.val
