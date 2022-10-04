# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recur(self, node, sm, target):

        if not node: 
            return False

        if not node.left and not node.right:
            return True if (sm + node.val) == target else False
        
        sm += node.val

        return self.recur(node.left, sm, target) or self.recur(node.right, sm, target)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.recur(root, 0, targetSum)
        