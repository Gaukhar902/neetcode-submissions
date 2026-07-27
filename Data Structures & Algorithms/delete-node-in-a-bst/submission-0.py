# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: node not found
        if not root:
            return None

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            # Case 1: no left child -> return right child (could be None)
            if not root.left:
                return root.right
            # Case 2: no right child -> return left child
            if not root.right:
                return root.left

            # Case 3: two children
            # Find in-order successor (smallest in right subtree)
            successor = self._find_min(root.right)
            root.val = successor.val            # copy value
            # Delete the successor from the right subtree
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def _find_min(self, node: TreeNode) -> TreeNode:
        # Keep going left until no left child
        while node.left:
            node = node.left
        return node