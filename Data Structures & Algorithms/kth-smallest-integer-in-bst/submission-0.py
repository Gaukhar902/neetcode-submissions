# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # go as deep as possible to the left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # pop the smallest unvisited node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # move to the right subtree (next greater values)
            curr = curr.right