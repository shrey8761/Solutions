# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

            # funtion to form binary tree
            # passing start point and end point that is the range with in which we can form a tree
            def DFS(start, end):

                # base case if start is greater then end the return none as a list
                if start > end: return [None]

                # dummy list to store all the sub trees
                ans = list()

                # now iterate over all the element from start to end + 1
                for i in range(start, end + 1):

                    # call the funtion recursively for left and right
                    # form start to current element - 1 respectively parameter for left
                    # and from current element + 1 to end respectively parameter for right
                    left = DFS(start, i - 1)
                    right = DFS(i + 1, end)

                    # iterate over each subtree and in left and right and form a tree and append the 
                    # tree to ans list
                    for l in left:
                        for r in right:

                            root = TreeNode(i)
                            root.left = l
                            root.right = r
                            ans.append(root)

                # return the ans list
                return ans

            # call the funtion
            return DFS(1,n)        