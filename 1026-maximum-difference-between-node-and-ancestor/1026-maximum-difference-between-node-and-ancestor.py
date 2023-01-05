# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        if not root:
            return 0
        
        def helper(curr,curr_min,curr_max):
            if not curr:
                return

            curr_min = min(curr.val,curr_min)
            curr_max = max(curr.val,curr_max)
            self.result = max(self.result,abs(curr_min-curr.val), abs(curr_max-curr.val))
            
            
            helper(curr.left,curr_min,curr_max)
            helper(curr.right,curr_min,curr_max)
        
        helper(root,root.val,root.val)
        
        return self.result
            
        
        