# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#     This is first way
        # if root is None:
        #     return 0
        # return 1+(max(self.maxDepth(root.left),self.maxDepth(root.right)))
        
# This is seconf way
        if root is None:
            return 0
        
        d = deque([root])
        ans = 0
        while d:
            for i in range(len(d)):
                node = d.pop()
                if node.left:
                    d.appendleft(node.left)
                if node.right:
                    d.appendleft(node.right)
            ans += 1
        return ans
            
            
        